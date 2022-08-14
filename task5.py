# TASK 5
# Create a new file "task5.py".
# - Write a Python function with the name "en_filter" which takes one parameter and checks whether a string has no "e" and "n".
# - Use a list comprehension which loops through the previous list from task 3 (community_members) and call (use) that function in the list comprehension.
#
# If the requirements are met, extend the function "en_filter" by implementing the code to append the string variable to the new list, created by the list comprehension. Print the final list.
#
# Hint:  You have to use the 'return' statement...

community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]


def en_filter(x):
    if "e" not in x and "n" not in x:
        return x
    else:
        return "empty"


final_list = [en_filter(y) for y in community_members]
print(final_list)
