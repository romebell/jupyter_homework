#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    if(n == 1):
        return n
    else:
        return n * factorial(n-1)


# In[2]:


print(factorial(5))


# In[3]:


print(factorial(7))


# In[4]:


print(factorial(3))


# In[7]:


def find_max(l):
    if (len(l) == 1):
        return l[0]
    return max(l[0],find_max(l[1:]))


# In[8]:


print(find_max([1, 4, 45, 6, -50, 10, 2]))


# In[9]:


print(find_max([1, 4, 4, 6, -20, 17, 8, 22, 22]))


# In[10]:


print(find_max([1125, 490, 458, 665, -506, 1056, 234]))


# In[11]:


def fib(n):
    if (n <= 0):
        return 0
    elif (n <= 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)


# In[12]:


print(fib(-1))


# In[13]:


print(fib(7))


# In[14]:


print(fib(2))


# In[15]:


print(fib(0))


# In[16]:


print(fib(1))


# In[17]:


print(fib(20))


# In[18]:


print(fib(10))


# In[ ]:




