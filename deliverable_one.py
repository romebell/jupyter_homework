#!/usr/bin/env python
# coding: utf-8

# # Hangman Challenge
# 
# You will be building the classic hangman game in Python. In hangman, a secret word is chosen and the user tries to guess each letter. Each correct guess reveals all instances of that letter. Each incorrect guess draws another body part on the poor guy getting hanged. The user wins if they reveal the entire word. They lose if the whole person is drawn on the noose.

# In[9]:


import random


# In[10]:


import time


# In[11]:


words = ('apple', 'banana', 'orange', 'mississippi', 'washington')
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("")
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
random_word = random.choice(words)
ls =[]


# In[12]:


# defining a function for words to display and words with underscores


# In[13]:


def display_word():
    display = ""
    for i in random_word:
        letter = i
        if letter in ls:
            display += letter
        else:
            display += '_'
    print(display)

display_word()


# In[ ]:


#  defining a function with a guess letters

def guess_letter():
    turns = 6
    while turns > 0:
        letter = input('Guess a letter: ')
        if letter not in random_word:
            turns -= 1
            ls.append(letter)
            print(ls)
            display_word()
            print('Wrong, sorry try again')
            print('You have', + turns, 'more guesses')
        elif letter in random_word:
            turns -= 1
            ls.append(letter)
            print(ls)
            display_word()
            print('You got it right let\'s try again', + turns )
        if letter == random_word:
            print('You won!')
            
        print(ls)
guess_letter()

