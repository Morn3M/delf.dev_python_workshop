# 2. Given is a list between numbers from 0 to 100. All numbers which have a 5 as a digit like: 5, 15, 95 should be counted and stored in a new list variable.
# Please return the total number of entries in that list and the list itself.
# Hint: Python "in" statement
# Example: if "maple" in "maplestory":

final_list = []

for i in range(101):
    if '5' in str(i):
        final_list.append(i)

print(final_list)
print(len(final_list))