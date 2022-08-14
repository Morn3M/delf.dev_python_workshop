# DAY 3, TASK 3+4
# Please create a new file for each task. [task3.py and task4.py]
#
# TASK 3
# 3. Given is a list called community_members with names of our members (strings) in it.
# All members which have at least the letter "a" 1x in should be filtered and stored in a new list variable.
# Please return the total number of entries of that list. Please copy the list down below in the example for your  community_members.
#
# Hint:
# Use a for loop again and the "in" operator
# Documentation:https://www.w3schools.com/python/python_for_loops.asp
#
# Example:
# ❌ "long" does not include the letter "a"
# ✅ "blazertherazer12" does include the letter "a" twice.
# ✅ "starving" does include the letter "a" once.
#
# # COPY THIS
# community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]

community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]

final_list = []

for some_variable in community_members:
    if "a" in str(some_variable):
        final_list.append(some_variable)

print(final_list)
print(len(final_list))