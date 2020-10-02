# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:02:54 2020

@author: striver
"""



A=[[1,1,1],[1,1,0],[1,1,0]]
n=len(A)

def find_k(A):
    t=1
    while t<n:
        k=t
        if t>n//2:
            return n
        if n%t!=0:
            t+=1
            continue
        while A[:k]==A[k:2*k][::-1]:
            if 2*k==n:
                return t
            if n%k != 0:
                break
            k=2*k
        t+=1
if n>1:
    ans=find_k(A)
else:
    ans=1
for i in range(ans):
    x=[str(i)  for i in A[i]]
    print(' '.join(x))

