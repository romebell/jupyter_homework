#!/usr/bin/env python
# coding: utf-8

# In[44]:


from selenium import webdriver


# In[15]:


import json, re, datetime, time, requests


# In[16]:


driver = webdriver.Chrome(executable_path='/Users/subrataroy/Downloads/chromedriver')


# In[17]:


driver.get('https://www.facebook.com/')


# In[18]:


from keys import instagram_username, instagram_password


# In[19]:


username = driver.find_element_by_xpath('//*[@id="email"]')
username.send_keys(instagram_username)


# In[20]:


password_input = driver.find_element_by_xpath('//*[@id="pass"]')
password_input.send_keys(instagram_password)


# In[21]:


login_button = driver.find_element_by_xpath('//*[@id="u_0_b"]')
login_button.click()


# In[23]:


post_div = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[60]/div/div/div/div/div/div/div/div/div/div/div[2]/div').text
print(post_div)


# In[25]:


post_list = post_div.split('\n')
print(post_list)


# In[55]:


name = post_list[1]
print(name)
description = post_list[-11]
print(description)
image_description = post_list[-9]
print(image_description)
likes = post_list[-7]
print(likes)
comments = post_list[-5]
print(comments)
shares = post_list[-4]
print(shares)


# In[53]:


post_image = driver.find_element_by_xpath('//*[@id="jsc_c_164"]/div[1]/div[1]/div/div/a/div[1]/div/div/div/img[starts-with(@src,"https")]')
print(post_image)

# not printing image url


# In[26]:


import pymongo


# In[27]:


myclient = pymongo.MongoClient('mongodb://localhost:27017/')


# In[29]:


mydb = myclient['jupyter_notebook']


# In[30]:


facebook_post = mydb['facebook_post'] 


# In[56]:


data = {
    "name": name,
    "description": description,
    "image_url": "null",
    "image_description": image_description,
    "likes": likes,
    "comments": comments,
    "shares": shares
}


# In[57]:


facebook_post.insert_one(data)


# In[62]:


print(facebook_post.find_one())


# In[ ]:




