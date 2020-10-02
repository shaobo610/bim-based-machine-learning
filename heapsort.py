# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:19:35 2020

@author: striver
"""

def heapify(tree, n, i):
    if i>=n:
        return
    c1 = 2*i+1
    c2 = 2*i+2
    max_=i
    if c1 < n and tree[c1] > tree[max_]:
        max_ = c1
    if c2 < n and tree[c2] > tree[max_]:
        max_ = c2
    if max_ != i:
        tree[i],tree[max_]=tree[max_],tree[i]
        heapify(tree, n, max_)

def build_heap(tree, n):
    last_node=n-1
    parent=(last_node-1)//2
    for i in range(parent,-1,-1):
        heapify(tree,n,i)

def heap_sort(tree, n):
    build_heap(tree,n)
    for i in range(n-1,-1,-1):
        tree[0],tree[i]=tree[i],tree[0]
        heapify(tree,i,0)

    
tree=[4,10,3,5,1,2]
n=6
#heapify(tree,n,0)
#build_heap(tree,n)
heap_sort(tree,n)
for i in range(n):
    print(tree[i])
