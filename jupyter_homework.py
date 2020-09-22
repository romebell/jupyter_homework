#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver


# In[4]:


def countdown(num):
    # base cause
    if num == 0:
        print('Blast off!')
        return 
    
    # recursive step
    print(num)
    countdown(num - 1)

countdown(10)


# In[5]:


def countdown(num):
         # base cause
    if num == 0:
        print('Blast off!')
        return 
    elif num < 0:
        print('Please add a positive and try again')
        return
    # recursive step
    print(num)
    countdown(num - 1)
countdown(100)
# countdown(-10)


# In[6]:


def countdown(num):
         # base cause
    if num == 0:
        print('Blast off!')
        return 
    elif num < 0:
        print('Please add a positive and try again')
        return
    # recursive step
    print(num)
    countdown(num - 1)
# countdown(100)
countdown(-10)


# In[8]:


numbers = [1,2,3,4,5]

def add_number(numbers_array, result=0):
    num = numbers_array.pop() # 5
    result += num # 5
    # base case
    if len(numbers_array) == 0:
        return result

    # recursive step
    return add_number(numbers_array, result)
    
print(add_number(numbers))


# In[ ]:




