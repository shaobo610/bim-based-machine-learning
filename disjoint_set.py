# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:06:07 2020

@author: striver
"""

#Disjoint set
def initialize(vertices):
    parent = [-1 for _ in range(vertices)]
    rank = [0 for _ in range(vertices)]
    return parent,rank
def find_root(x):
    while parent[x] != -1:
        x = parent[x]
    return x
def union_set(x, y, parent, rank):
    x_root = find_root(x)
    y_root = find_root(y)
    if x_root == y_root:
        return 0 
    else:
        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
            
        elif rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        else:
            parent[x_root] = y_root
            rank[x_root] += 1
        
def main(vertices, edges, parent, rank):
    for i in range(len(edges)):
        if union_set(edges[i][0], edges[i][1], parent, rank) == 0:
            print("Cycle detected!")
            return
    print("No cycles found")
    
if __name__ == '__main__':
    #edges = {0:1, 1:2, 1:3, 2:4, 3:4, 2:5 }
    vertices = 6
    edges = [[0,1], [1,2], [1,3], [5,4],[3,4], [2,5]]
    parent, rank = initialize(vertices)
    main(vertices, edges, parent, rank)

        
    
    