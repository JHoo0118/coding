#Given an array of integers, find the first missing positive integer 
#in linear time and constant space. In other words, 
#find the lowest positive integer that does not exist in the array. 
#The array can contain duplicates and negative numbers as well.
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#You can modify the input array in-place.

input_list = [-2, 0, 2, 3]
input_list.sort()

# -1, 1, 3, 4
def lowest_positive_number(input_list):
    if input_list[-1] <= 0:
        return 1
    for i in range(len(input_list) - 1):
        if input_list[i+1] - input_list[i] >= 2 and input_list[i+1] >= 0 and input_list[i] > -1:
            return input_list[i] + 1
    return input_list[-1] + 1

nums = [-2, 0, 2, 3]

def first_missing_positive(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i

print(lowest_positive_number(input_list))
print(first_missing_positive(nums))