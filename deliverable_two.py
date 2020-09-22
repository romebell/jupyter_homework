#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import shuffle
tries = 0


# In[2]:


def is_sorted(ls):
    # Loop through the list
    # Make sure each item is less than (or equal) to the next
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]: return False
    return True


# In[3]:


def bogo_sort(ls):
    global tries
    tries += 1
    # check if already sorted
    if is_sorted(ls): return ls
    # if not, shuffle list + check again!
    shuffle(ls)
    return bogo_sort(ls)


# In[8]:


test = [1, 43, 23, 5, 2, 6, 15]


# In[10]:


print(test)


# In[11]:


print('It is ', bogo_sort(test), ' Sort was found after ', tries, ' tries')


# In[ ]:




