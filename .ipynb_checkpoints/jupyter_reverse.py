#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do.


# In[9]:


my_str = input('Enter a string: ')


# In[10]:


temp = ''


# In[11]:


for char in my_str:
    temp = char + temp
print(temp)


# In[ ]:




