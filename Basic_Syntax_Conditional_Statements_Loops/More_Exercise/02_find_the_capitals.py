my_string = input()

indices_list = []

for index in range(len(my_string)):
    if my_string[index].isupper():
        indices_list.append(index)

print(indices_list)
