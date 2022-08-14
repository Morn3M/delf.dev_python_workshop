# Task7

# B) 📁Save your data - Learning how to write and save into a file. 📁
# Create a new file called python7b.py and write a new function called save_list_into_file(my_list) with one parameter which should be a list.
# After that, check out task 5 again and save the result of that task (the filtered list) into a new file called my_first_saved_list.txt.


community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]


def en_filter(x):
    if 'e' not in x and 'n' not in x:
        return x
    else:
        return 'empty'


final_list = [en_filter(y) for y in community_members]

f_list = [f for f in final_list if f.strip() != 'empty']

print(f_list)


def save_list_into_file(my_list: list):
    with open('my_first_saved_list.txt', 'w') as f:
        f.write(str(my_list))


save_list_into_file(f_list)
