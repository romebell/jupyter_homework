#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1, Loop

def p_times():
    user_statement = input("Enter a statement: ")
    number = int(input("Enter how many times: "))
    for _i in range(1, number + 1):
        print(user_statement)


# In[2]:


p_times()


# In[3]:


dd = {}

def letter_count(string):
    global dd

    for letter in string:
        if letter not in dd:
            dd[letter] = 1
        elif letter in dd:
            dd[letter] +=1
    return dd


# In[4]:


print(letter_count("Hello"))


# In[5]:


# Question 3, Print Contacts

contacts = {
  'Brian': '333-333-3333',
  'Lenny': '444-444-4444',
  'Daniel': '777-777-7777'
}

def print_contacts(phonebook):
    for contact in phonebook:
        if contact in phonebook:
            value = phonebook[contact]
            print(f"{contact} has a phone number of {value}")
        


# In[6]:


print_contacts(contacts)


# In[7]:


#Question 4, Multiply By

my_array = [2, 14, 3]

def multiply_by(array, num):
    print(list(map(lambda x: x * num, array)))


# In[8]:


multiply_by(my_array, 2)


# In[9]:


# Alternate way to do problem 4

my_array2 = [2, 14, 3]
my_new_array = []

def multiply_by2(array, num):
    for number in array:
       my_new_array.append(number * num)


# In[10]:


multiply_by2(my_array, 2)
print(my_new_array)


# In[11]:


def factory(n):
    new_num = 1
    for digit in range(1, n + 1):
        new_num *= digit
    return new_num


# In[12]:


print(factory(5))


# In[ ]:




