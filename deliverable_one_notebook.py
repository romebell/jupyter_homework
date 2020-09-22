#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Quick Sort Algorithm
nums = [3, 78, 23, 466, 324, 2, 12, 546, 17, 56, 23, 123, 343, 87, 94, 45, 6, 9, 234, 36]
# print(nums)


# In[12]:


def quick_sort(ls):
    # Base case
    if len(ls) <= 1:
        return ls
    pivot = ls.pop() # 9
    left = [x for x in ls if x <= pivot]
    # left = [3, 2]
    right = [y for y in ls if y > pivot]
    # right = [23, 12, 17, 23]
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    print('Result', left_sorted + [pivot] + right_sorted)
    return left_sorted + [pivot] + right_sorted
# quick_sort(nums) just to test that result left sorted and right sorted were printing


# In[13]:


quick_sort(nums)


# In[ ]:




