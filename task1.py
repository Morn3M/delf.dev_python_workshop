# Please create 2 files [task1.py and task2.py]  which run those tasks independently.
#
# 1. Given is a list between numbers from 0 to 100 and it should be output every number in the terminal, which is divisible by 2.
#
# Hint: Use a For Loop, if necessary research "Modulo".
# Examples: https://realpython.com/python-modulo-operator/

my_list = list(range(0, 101))
# print(my_list)
final_list = []

for i in my_list:
    if i % 2 == 0:
        final_list.append(i)
print(final_list)
