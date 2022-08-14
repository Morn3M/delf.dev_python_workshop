# TASK 6
# Create a new file "task6.py"
# - Given an empty list "random_values", write a Python function called "random_value_consumer" which takes 2 parameters of any data type in and adds the both parameters to that list.
# - Write a new function called "analyse_list_elements" which takes 1 parameter. The function should print the length of each element of that list with its value and type.
#
# Example:
# random_values = [5, "long"]
# # output:
# <class 'int'> 5  ->  1
# <class 'str'> long  -> 4
#
# Hint:  There is no hint. JEBAITED

random_values = []

def random_value_consumer(a:any,b:any):
    random_values.append(a)
    random_values.append(b)


random_value_consumer(9, 'Morne')
print(random_values)

def analyse_list_elements():
    for element in random_values:
        print(element, type(element), len(str(element)), sep='---')


analyse_list_elements()