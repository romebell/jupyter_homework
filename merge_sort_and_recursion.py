#!/usr/bin/env python
# coding: utf-8

# In[8]:


number = [1,2,3,4,5]


# In[10]:


def add_number(numbers_array, result=0):
    # result = 0
    # return what u took out
    num = numbers_array.pop()
    result += num
    #base case
    print('The length of array is {}'.format(len(numbers_array)))
    
    if len(numbers_array) == 0:
        print(result)
        return result
    
    # recursive step
    return add_number(numbers_array, result)
print(add_number(number))


# In[11]:


nums = [3, 78, 23, 466, 324, 2, 12, 546, 17, 56, 23, 123, 343, 87, 94, 45, 6, 9, 234, 36]


# In[12]:


def merge_sort(ls):
    # Base Case
    if len(ls) <= 1:
        return ls
    # Recursive Case
    # 1. Find the midpoint of the list
    mid = len(ls) // 2 # // is for integer division
    # 2. Divide the list in half
    left = ls[:mid] # :mid is shorthand for 0:mid
    print('left list: ', left)
    right = ls[mid:] # mid: is shorthand for mid - end of the list
    print('right list: ', right)
    # 3. Sort each side
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    # 4. Merge the two lists back together
    return merge(left_sorted, right_sorted)


# In[13]:


def merge(ls1, ls2):
    print('ls1: ', ls1)
    print('ls2: ', ls2)
    sort = []
    while len(ls1) and len(ls2):
        if ls1[0] > ls2[0]:
            sort.append(ls2.pop(0))
        else:
            sort.append(ls1.pop(0))
    sort = sort + ls1 + ls2
    print('Sorted List: ', sort)
    return (sort)
merge_sort(nums)


# In[ ]:




