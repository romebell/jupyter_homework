#!/usr/bin/env python
# coding: utf-8

# In[1]:


class PancakePlate():
    def __init__(self, amount, type):
        self.pancake_stack = amount
        self.pancake_type = type
        self.is_amazing = False

    def eat(self, amount):
        self.pancake_stack -= amount

    def addPancakes(self, amount, type):
        self.pancake_stack += amount
        self.pancake_type = type

    def addSyrup(self):
        self.is_amazing = True


# In[3]:


anthony_plate = PancakePlate(10, "chocolate_chip")


# In[5]:


print(anthony_plate.pancake_stack)


# In[ ]:




