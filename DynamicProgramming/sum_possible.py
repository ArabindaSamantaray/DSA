"""
Write a function sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.
"""


def sum_possible(target, list_of_numbers, memo={}):
    if target==0:
        return True
    elif target<0:
        return False
    elif target in memo:
        memo[target]
    else:
        for number in list_of_numbers:
            memo[target-number] = sum_possible(target-number, list_of_numbers, memo)
            if memo[target-number]:
                return True
        return False

print(sum_possible(8, [5, 12, 4])==True)
print(sum_possible(15, [6, 2, 10, 19])==False)
print(sum_possible(12, [])==False)
print(sum_possible(271, [10, 8, 265, 24])==False)
print(sum_possible(2017, [4, 2, 10])==False)
