#!/usr/bin/env python
# coding: utf-8

# In[53]:


'''
  Given a greph find if it has eulerian path or eulearian cycle
'''

class Graph:
    def __init__(self,nodes):
            self.nodes = nodes
            self.adj_list= {}
            for node in self.nodes:
              self.adj_list[node] = []
            
    def addEdge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def print(self):
        for node in self.nodes:
            print(node, "-->", self.adj_list[node])
            
    def hasEulerianCycle(self):
        odd = 0
        for v in self.adj_list:
            if len(self.adj_list[v]) %2 == 1:
                #odd = odd+1
                odd = 1
                break
                
        if odd == 0:
           return True
        else:
           return False
    
    def hasEulerianPath(self):
        odd = 0
        for v in self.adj_list:
            if len(self.adj_list[v]) %2 == 1:
                odd = odd+1
                                
        if odd == 0 or odd ==2:
           return True
        else:
           return False
    

                
     
        
#nodes = ["1", "2", "3", "4"]
#Edges = [ ("1","2"), ("2","3"),("3","4"),("4","1"), ("1","3")]

nodes = ["A", "B", "C", "D"]
Edges = [ ("A","B"), ("B","C"),("C","D"),("D","A"), ("A","C")]

g = Graph(nodes)
for u, v in Edges:
    g.addEdge(u,v)
g.print()

print(g.hasEulerianCycle())
print(g.hasEulerianPath())





# A----B
# |    |
# |    |
# D----C
 
#above has eulerian cyccle but next one if we connectthe diagonal AC then it is not    
    
    
# A----B
# |    |
# |    |
# D----C
    


# In[ ]:





# In[ ]:




