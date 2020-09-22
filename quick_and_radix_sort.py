#!/usr/bin/env python
# coding: utf-8

# In[18]:


nums = [413, 445, 403, 224, 157, 312, 785, 862, 602]


# In[19]:


def quick_sort(ls):
    # Base case
    if len(ls) <= 1:
        return ls

    pivot = ls.pop() # 9
    left = [x for x in ls if x <= pivot]
    # left = [3, 2]
    right = [y for y in ls if y > pivot]
    # right = [23, 12, 17, 23]

    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    print('Result', left_sorted + [pivot] + right_sorted)
    return left_sorted + [pivot] + right_sorted

quick_sort(nums)


# In[20]:


def radix_sort(ls):
    # Determine k (length of longest number)
    k = len(str(max(ls)))
    # Start a k loop
    print('this is k: ', k)
    for i in range(k):
        # Make buckets for values 0-9
        buckets = make_buckets()
        # Make inner n loop
        for j in range(len(ls)):
            # Determine the "place" we're looking at
            place = 10**i
            # Chop down the number to the correct digit
            digit = ls[j] // place
            # Get the bucket number
            bucket_num = digit % 10
            # Place the value into the correct bucket
            buckets[bucket_num].append(ls[j])
        # Mash the buckets together
        ls = flatten(buckets)
    return ls

def flatten(buckets):
    flat = []
    for bucket in buckets:
        flat += bucket
        print(flat)
    return flat 

def make_buckets():
    buckets = []
    for i in range(10):
        buckets.append([])
    return buckets
print('Sorted list: ', radix_sort(nums))


# In[ ]:




