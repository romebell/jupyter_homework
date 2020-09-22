#!/usr/bin/env python
# coding: utf-8

# In[1]:


# define a calculator function
def calculator():
#     make input to ask user what operation and number to solve
    calc = input('What operation would you like to do? (add, sub, multiply, divide)\n')
    num1 = input('Your first number\n')
    num2 = input('Your second number\n')
    if calc == 'add':
        result = int(num1) + int(num2)
    elif calc == 'sub':
        result = int(num1) - int(num2)
    elif calc == 'multiply':
        result = int(num1) * int(num2)
    elif calc == 'divide':
        result = int(num1) / int(num2)
    return result
print(calculator())

