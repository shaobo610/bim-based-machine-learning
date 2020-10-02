# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 20:27:19 2020

@author: striver
"""

import numpy as np
#n,th=input().split()
#n,th=int(n),float(th)
#nums=[]
#for _ in range(n):
#    nums.append(list(map(float,input().split())))

n,th=3,0.3
nums=[[50.0,51.0,180.0,200.0,0.9],
[48.0,53.0,170.0,210.1,0.8],
[200.0,51.0,242.1,81.0,0.7]]
boxes=np.array(nums)
x1=boxes[:,0]
y1=boxes[:,1]
x2=boxes[:,2]
y2=boxes[:,3]
scores=boxes[:,4]
area=(x2-x1+1)*(y2-y1+1)

order=np.argsort(scores)
ans=[]
while order.size>0:
    ind=order[-1]
    ans.append(nums[ind])
    x11=np.maximum(x1[ind],x1[order[:-1]])
    y11=np.maximum(y1[ind],y1[order[:-1]])
    x22=np.minimum(x2[ind],x2[order[:-1]])
    y22=np.minimum(y2[ind],y2[order[:-1]])
    jiaocha=np.maximum(0,x22-x11+1)*np.maximum(0,y22-y11+1)
    iou=jiaocha/(area[ind]+area[order[:-1]]-jiaocha)
    l=np.where(iou<th)
    order=order[l]
for i in range(len(ans)):
    for j in range(5):
        ans[i][j]=str(ans[i][j])
for i in ans:
    print(' '.join(i))