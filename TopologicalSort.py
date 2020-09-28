#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
   Topological sort where we produce a linear ordering of all the vertices so that if two vertices u
    and v are there in the list then u comes before v
'''

from collections import deque

#vertices is the vertex count
#edges is like (1,2) , (2,3)
def topological_sort(vertices, edges):
    sortedorder = []
    if vertices <= 0:
        return sortedorder
    
    #initialize the graph    
    indegree = { i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    #build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        indegree[child] += 1
    
    #c Find all sources ie all vertices with 0 degree
    sources = deque()
    for key in indegree:
        if indegree[key] == 0:
            sources.append(key)
        
        
    while sources:
        vertex =  sources.popleft()
        sortedorder.append(vertex)
        # get the node's childreen to decrement their in degree
        for child in graph[vertex]:
            indegree[child] -= 1
            if indegree[child] == 0:
                sources.append(child)
            
            
    # topologcal sort is not possible as the graph has a cycle
    if len(sortedorder)  != vertices:
        return []
    
    return sortedorder

def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
    
       


# In[ ]:




