"""
Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.

The 0-th and 1-st numbers of the sequence are both 0.

The 2-nd number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous three numbers.

Solve this recursively.
"""

def tribonacci(n, memo={}):
    if n<=1:
        return 0
    elif n==2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n]= tribonacci(n-1, memo)+tribonacci(n-2, memo)+tribonacci(n-3, memo)
        return memo[n]


print(tribonacci(0)==0)
print(tribonacci(1)==0)
print(tribonacci(2)==1)
print(tribonacci(5)==4)

print(tribonacci(20)==35890)
print(tribonacci(37)==1132436852)
