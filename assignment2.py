
# In[4]:


def fib(n):
    # Write code here
    #base
    if n < 0:
        return 0
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

fib(4)


# In[ ]:
