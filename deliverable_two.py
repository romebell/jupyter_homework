# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number
# For this function, the first two fibonacci numbers are 1 and 1

def fib(n):
    # Write code here
    #base
    if n < 0:
        return 0
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
    # increment = n

print(fib(-1))
# => 0
print(fib(0))
# => 0
print(fib(1))
# => 1
# => 1
print(fib(7))
# => 13