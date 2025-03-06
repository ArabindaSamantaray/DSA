"""
Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively.


"""

def fib(n, memo={}):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n in memo.keys():
        return memo[n]
    else:
        memo[n]= fib(n-1, memo)+fib(n-2, memo)
        return memo[n]

print(fib(0)==0)
print(fib(1)==1)
print(fib(2)==1)
print(fib(3)==2)
print(fib(4)==3)
print(fib(5)==5)
print(fib(35)==9227465)
print(fib(46)==1836311903)
