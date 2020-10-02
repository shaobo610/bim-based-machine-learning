# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:21:57 2020

@author: striver
"""

#while True:
#    try:
#        n,m,k=map(int,input().split())
#        A=list(map(int,input().split()))
m,k=6,5
A=[5,5,5,5,5,4,6,5,9,3]
n=len(A)
re=0
fuzhu=[0]*(n+1)
for i in range(n):
    if A[i]>=k:
        fuzhu[i]=1
i=0
while i<n:
    if fuzhu[i]:
        temp=i
        while fuzhu[i]:
            i+=1
        if i-temp>=m:
            re+=i-temp-(m-1)
    else:
        i+=1
print(re)

#    except:
#        break