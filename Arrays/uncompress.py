"""
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:
<number><char>

for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
"""

def get_total_count(input_data, index):
    sum_of_digits = 0
    while input_data[index].isdigit():
        sum_of_digits = sum_of_digits * 10 + int(input_data[index])
        index = index+1
    return (sum_of_digits, index)


def uncompress(input_data):
    final_string=""
    index = 0
    while index<len(input_data):
        if input_data[index].isdigit():
            count, index = get_total_count(input_data, index)
            final_string=final_string+count*input_data[index]
            index = index+1
    return final_string

print(uncompress("2c3a1t")=="ccaaat")
print(uncompress("4s2b")=="ssssbb")
print(uncompress("2p1o5p")=="ppoppppp")
print(uncompress("3n12e2z")=="nnneeeeeeeeeeeezz")
print(uncompress("127y")=="yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")


