# TASK 4
# 4. Given is a list called "list_99" between numbers from 0 to 100. Create a new list variable and code the following case:
# a) All numbers which have a 9 as a digit like: 9, 19, 99 should be counted, multiplied by 2 and stored in a new list variable.
# Output The new list should look like this; numbers_5_only = [18, 38, 28, 58.. ...198]
#
# b) Return  (print)  the very last element of that list only.
# Output 198
# Hint: Use slicing operators in Python: my_list[-1]
#
# extra) All numbers which have a 7 as a digit like 7, 17, 97 should be removed from the previous list "list_99". Your goal is to get a new list without the 7's.
# Output The new list should look like this numbers_without_7 = [0,1,2,3,4,5,6,8,9....96,98,99]
#
# Hint: You can use multiple if cases.

list_99 = range(101)

new_list = []
numbers_without_7 = []

for i in list_99:
    if "9" in str(i):
        new_list.append(i * 2)
    if "7" not in str(i):
        numbers_without_7.append(i)

print(new_list)

print(new_list[-1])

print(numbers_without_7)
