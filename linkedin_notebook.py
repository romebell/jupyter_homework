#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[3]:


import json, re, datetime, time, requests


# In[4]:


driver = webdriver.Chrome(executable_path='/Users/subrataroy/Downloads/chromedriver')


# In[5]:


driver.get('https://www.linkedin.com/')


# In[7]:


from keys import linkedin_email, linkedin_password


# In[8]:


email_input = driver.find_element_by_xpath('//*[@id="session_key"]')
email_input.send_keys(linkedin_email)


# In[9]:


password_input = driver.find_element_by_xpath('//*[@id="session_password"]')
password_input.send_keys(linkedin_password)


# In[10]:


login_button = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button')
login_button.click()


# In[11]:


skip = driver.find_element_by_xpath('//*[@id="ember510"]/button[2]')
skip.click()


# In[14]:


post_div = driver.find_element_by_xpath('//*[@id="ember668"]').text
post_list = post_div.split('\n')
print(post_list)


# In[29]:


name = post_list[1]
print(name)
user_details = post_list[3]
print(user_details)
description = " ".join(post_list[6:11])
print(description)
likes = post_list[13]
print(likes)


# In[15]:


import pymongo


# In[16]:


myclient = pymongo.MongoClient('mongodb://localhost:27017')


# In[26]:


mydb = myclient['jupyter_notebook']
linkedin_collection = mydb['linkedin_post']


# In[36]:


linkedin_collection.insert_one({
    "name": name,
    "user_details": user_details,
    "description": description,
    "likes": likes
})


# In[37]:


linkedin_collection.find_one()


# In[ ]:




