num = [3, 78, 23, 466, 324, 2, 12, 546, 17, 546, 17, 56, 23, 123, 343, 87, 94, 45, 6, 9, 234, 36]
def bubble_sort(ls):
    n = len(ls)
    # Traverse the entire array and all items within it
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1, since i has already been traversed, this will be the comparison for each value i
            # Swap if the element found is greater than the next element
            if ls[j] > ls[j+1] : 
                ls[j], ls[j+1] = ls[j+1], ls[j] 
    print('Sorted List: ')      
    print(ls)
    return ls
def bubble_sort2(ls):
    # Loop through each element in the list
    for i in range(len(ls)):
        # Track whether anything has been swapped this round
        swapped = False
        for j in range(len(ls)-i-1):
            # If it needs a swap, swap it
            if ls[j] > ls[j+1]:
                ls[j], ls[j + 1] = ls[j+1], ls[j] # shorthand for swaps in python
                swapped = True
        # If you can break out early, do it
        if not swapped: break
    return ls
print(bubble_sort2(num))