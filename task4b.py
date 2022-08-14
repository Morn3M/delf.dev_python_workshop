list_99 = list(range(101))

new_list = []
# numbers_without_7 = []

for i in list_99:
    if "9" in str(i):
        new_list.append(i * 2)

print(new_list)

print(new_list[-1])

list_99.remove(7)
print("numbers_without_7: ", list_99)
