#!/usr/bin/env python
# coding: utf-8

# In[1]:


def p_times(num, statement):
    for i in range(num):
        print(statement)
        


# In[2]:


p_times(7, "Boots and Cats and")
p_times(4, "THANKS PETE")
p_times(2, "Let's GOOOOOOOOOOO")


# In[3]:


def letter_count(string):
  dd= {}
  for letter in string:
      if (letter in dd):
        dd[letter] = dd[letter] + 1
      else:
        dd[letter] = 1

  print(dd)


# In[4]:


letter_count("Camp Wannahockalugee")
letter_count("I never meant to start a war")
letter_count("Sweet dreams")


# In[5]:


contacts = {
  'Brian': '333-333-3333',
  'Lenny': '444-444-4444',
  'Daniel': '777-777-7777'
}


# In[6]:


def print_contacts(contacts):
  # print(arguments)
  for key in contacts:
    print(f"{key} has a phone number of {contacts[key]}")
    


# In[7]:


print_contacts(contacts)


# In[8]:


def multiply_by(list, number):
   new_list = []
   for num in list:
        # print(item)
       new_list.append(num * number)
   return new_list


# In[9]:


print(multiply_by([1,2,3], 5))
print(multiply_by([2,4,6], 10))
print(multiply_by([3,6,9], 15))


# In[10]:


def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


# In[11]:


print(factorial(7))
print(factorial(3))
print(factorial(11)) 


# In[ ]:




