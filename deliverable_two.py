#!/usr/bin/env python
# coding: utf-8

#  Use the `input()` function to prompt a user to enter something.
#  input() always returns a string value. If you ever want someone
#  to enter a number you have to use the `int()` function to convert
#  what they typed in to a string.

# In[ ]:


# define a calculator function
def calculator():
#     make input to ask user what operation and number to solve
    calc = input('What operation would you like to do? (add, sub, mult, div)\n')
    num1 = input('Your first number\n')
    num2 = input('Your second number\n')
    if calc == 'add':
        result = int(num1) + int(num2)
    elif calc == 'sub':
        result = int(num1) - int(num2)
    elif calc == 'mult':
        result = int(num1) * int(num2)
    elif calc == 'div':
        result = int(num1) / int(num2)
    return result
print(calculator())


# In[ ]:




