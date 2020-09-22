#!/usr/bin/env python
# coding: utf-8

# In[1]:


def reverse(ss):
    if len(ss) == 0:
        return ss
    return reverse(ss[1:]) + ss[0]


# In[2]:


print(reverse("")) 


# In[3]:


print(reverse("ab")) 


# In[4]:


print(reverse("aba")) 


# In[5]:


print(reverse("amazing")) 


# In[6]:


print(reverse(reverse("computer")))


# In[9]:


def coin_flips(n):
  if n <= 0:
    return []
  if n == 1:
    return ['H', 'T']
  combos = coin_flips(n - 1)
#   print(n)
  return [x + 'H' for x in combos] + [x + 'T' for x in combos]


# In[10]:


print(coin_flips(4))


# In[11]:


print(coin_flips(1))


# In[12]:


print(coin_flips(2))


# In[13]:


print(coin_flips(3))


# In[14]:


def pretty_print(dictionary, indent):
  for key in dictionary:
    value = dictionary[key]
    if isinstance(value, dict):
      print(f'{indent}{key}')
      pretty_print(value, indent + indent)
    else:
      print(f'{indent}{key}: {value},')


# In[15]:


o1 = {"a": 1, "b": 2}

o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}

o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}


# In[17]:


pretty_print(o1, "-")


# In[19]:


pretty_print(o2, "...")


# In[20]:


pretty_print(o3, "~~")


# In[ ]:




