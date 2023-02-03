some_string = input().split()

inverted_values_list = []

for el in some_string:
    number = int(el)

    if number == 0:
        inverted_values_list.append(number)
    elif number > 0:
        inverted_values_list.append(0 - abs(number))
    elif number < 0:
        inverted_values_list.append(0 + abs(number))

print(inverted_values_list)
