#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random


# In[7]:


secret_words = ['word', 'banana', 'divorce', 'cat', 'dinosaur']
random_word = random.choice(secret_words)
output = list('_'*len(random_word))
hang_array = ['  O\n\( )/\n / \\', '  O\n\( )/\n /', '  O\n\( )/', '  O\n ( )/', '  O\n ( )', ' O']


# In[8]:


def hang_man():
    print(random_word)
    print(' '.join(output))
    if len(hang_array) > 0:
        while (hang_array):
            letter = str(input("Enter a Letter:\n"))
            if letter in random_word:
                for i, j in enumerate(random_word):
                    print(i, j)
                    if j is letter:
                        output[i] = letter
                        new_output = ''.join(output)
                        print(' '.join(output))
                        if new_output == random_word:
                            print("You've won!")
                            return
            else:
                print(letter + " is not in the word")
                print(hang_array.pop())
                print(' '.join(output))
                if len(hang_array) < 1:
                    print("You have lost, the word was {}, please try again.".format(random_word))
                    return


# In[9]:


hang_man()


# In[ ]:




