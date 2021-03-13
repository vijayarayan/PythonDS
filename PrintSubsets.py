#!/usr/bin/env python
# coding: utf-8

# In[65]:


all1 = []

def addElement(table):
    all1.append(table)
    print(all1)
    
    
def main():
    table = []
    table.append(1)
    table.append(2)
    addElement(table)
    print(all1)
    
    
main()
    


# In[83]:


import copy

all1 = []
def getSubsets(nums, i, res):
    if i == len(nums):
        print(res)
        ret = copy.deepcopy(res)
        all1.append(ret)
        return

    #exclude
    getSubsets(nums, i+1, res)
    #include   
    res.append(nums[i])
    getSubsets(nums, i+1, res)
    del(res[-1])
    
def getSubset(nums):
    result = []
    getSubsets( nums, 0 , result)
    
def main():
    nums = [1,2]
    getSubset(nums)
    print(all1)
    
main()

# In[ ]:





# In[ ]:




