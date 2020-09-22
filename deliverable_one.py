# sorts

import random

# bubble sort

# random list generator
def random_num(num, random_list=[]):
    if (num > 0):
        random_list.append(random.randint(-999, 999))
        return random_num(num - 1, random_list)
    return random_list

def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n):
        for j in range(0, n - i -1):
            # Swap if elements found are greater than previous elements
            if (num_list[j] > num_list[j + 1]):
                # Shorthand for swapping values in python
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list

# merge sort
def merge_sort(arr):
    # base case
    if (len(arr) <= 1):
        return arr
    # recursive case
    mid = len(arr) // 2
    left = arr[mid:]
    right = arr[:mid]

    # sort each side
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def merge(ls1, ls2):
    sorted_list = []
    # running a while loop until both list are empty
    while len(ls1) and len(ls2):
        if ls1[0] > ls2[0]:
            sorted_list.append(ls2.pop(0))
        else:
            sorted_list.append(ls1.pop(0))
    sorted_list = sorted_list + ls1 + ls2
    return sorted_list

print(bubble_sort(random_num(100)))
print(merge_sort(random_num(100)))
