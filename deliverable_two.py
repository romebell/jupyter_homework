# recursion

# coin flip possibilities
def coin_flips(n, results=["No Coin Flips"]):
    # base case
    if n <= 0:
        return results
    # initial recursive case
    elif (results == ["No Coin Flips"]):
        results = ["H", "T"]
        return coin_flips(n - 1, results)
    # other recursive cases
    length = len(results)
    results *= 2
    # add "H" to first half
    i = 0
    while (i < length):
        results[i] += "H"
        i += 1
    # add "T" to second half
    while (i >= length and i < len(results)):
        results[i] += "T"
        i += 1
    return coin_flips(n - 1, results)


# factorial
def factorial(n, result=1):
    # recursive case
    if n != 0:
        result *= n
        return factorial(n - 1, result)
    # base case
    else:
        return result


# find max

import random

# random list generator
def random_num(num, random_list=[]):
    if (num > 0):
        random_list.append(random.randint(-999, 999))
        return random_num(num - 1, random_list)
    return random_list

def find_max(l, max="Array is Undefined"):
    # base case
    if len(l) == 0: 
        return max
    # initial recursive case
    elif (len(l) > 0 and max == "Array is Undefined"): 
        max = l.pop()
        return find_max(l, max)
    # other recursive cases
    if (max < l[-1]): # in the middle of recursion
        max = l.pop()
        return find_max(l, max)
    l.pop()
    return find_max(l, max)

print(coin_flips(4))
print(factorial(5))
print(find_max(random_num(10)))
