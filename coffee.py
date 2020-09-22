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


# In[6]:


class CoffeeCup():
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def fill(self):
        self.amount = self.capacity

    def empty(self):
        self.amount = 0

    def drink(self, amount):
        self.amount -= amount
        if (self.amount <= 0):
            self.amount = 0
            print("Coffee cup is now empty")


# In[7]:


anthony_cup = CoffeeCup(10)


# In[8]:


anthony_cup.fill()


# In[9]:


anthony_cup.drink(3)


# In[10]:


print(anthony_cup.amount)


# In[ ]:




