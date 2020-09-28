#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.


Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.

'''


from heapq import *
def find_k_frequent_numbers(nums, k):
    #find the frequency of each number
    numFrequencyMap = {}
    for num in nums:
        numFrequencyMap[num] = numFrequencyMap.get(num,0)+1
        
    minHeap = []
    for num,frequency in numFrequencyMap.items():
        heappush(minHeap, (frequency, num))
        if len(minHeap) > k:
            heappop(minHeap)
            
    topnumbers = []
    while minHeap:
        topnumbers.append( heappop(minHeap)[1])
        
    return topnumbers

def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
    


# In[ ]:




