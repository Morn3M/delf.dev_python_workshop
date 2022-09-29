# B) Now you need to recall your memory and open the newly created .json file.
# Check the previous tasks again if you forgot. Read the dictionary from the .json file into a variable of your choice and iterate through the list of dictionaries.
# Print a text which could look like the following example down below for each member of the dictionary:

import json

with open('selfdev_members.json', 'r') as list:
    data = list.read()

print(type(data))

#Open Json file as dictonary

with open('selfdev_members.json') as json_file:
    data = json.load(json_file)

    # Print the type of data variable
    print("Type:", type(data))