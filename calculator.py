#!/usr/bin/env python
# coding: utf-8

# In[1]:


# define a calculator function
def calculator():
#     make input to ask user what operation and number to solve
    choose_calc = input('What operation would you like to do? (add, sub, multiply, divide)\n')
    num1 = input('Your first number\n')
    num2 = input('Your second number\n')
    if choose_calc == 'add':
        result = int(num1) + int(num2)
    elif choose_calc == 'sub':
        result = int(num1) - int(num2)
    elif choose_calc == 'multiply':
        result = int(num1) * int(num2)
    elif choose_calc == 'divide':
        result = int(num1) / int(num2)
    return result
print(calculator())

