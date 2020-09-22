#!/usr/bin/env python
# coding: utf-8

# In[1]:


def p_times(statement, num):
    for i in range(num):
        print(f'{statement}')

p_times('Hello there', 3)


# In[2]:


def letter_count(str):
     dd = {}
     for letter in str:
         if letter in dd:
             dd[letter] += 1
         else: 
             dd[letter] = 1
     print(dd)
letter_count('banana')


# In[3]:


def print_contacts(contacts):
  for name, phone in contacts.items():
    print(f'{name} has a phone number of {phone}')
  
contacts = {
  'Brian': '333-333-3333',
  'Lenny': '444-444-4444',
  'Daniel': '777-777-7777'
}
print_contacts(contacts)


# In[4]:


def multiply_by(list, num):
    for number in list:
        print(number * num)
multiply_by([1, 2, 3], 5)


# In[5]:


def factorial(num):
    i = num - 1
    while i > 0:
        num = num * i
        i -= 1
    print(num)
factorial(5)





