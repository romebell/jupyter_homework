#!/usr/bin/env python
# coding: utf-8

# In[1]:


def p_times(statement, num):
    for i in range(num):
        print(statement)
        
p_times("Hello There", 4)


# In[2]:


def letter_count(string):
  dd = {}
  for letter in string:
    if letter in dd:
      dd[letter] += 1
    else:
      dd[letter] = 1
  print(dd)

letter_count("Domingo")


# In[3]:


contacts = {
  'Brian': '333-333-3333',
  'Lenny': '444-444-4444',
  'Daniel': '777-777-7777'
}

def print_contacts(contact):
  for x, y in contacts.items():
    print(f"{x} has a phone number of", f"{y}")

print_contacts(contacts)


# In[4]:



def multiply_by(arr, num):
    newList = []

    for numbers in arr:   
        newList.append(numbers * num) 
    print(newList)

multiply_by([1,2,3,4], 5)


# In[5]:


import math

def factorial(n):
    return math.factorial(n) 

print(factorial(5))


# In[ ]:




