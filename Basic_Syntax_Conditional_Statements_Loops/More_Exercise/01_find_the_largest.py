numbers = int(input())

numbers_as_string = str(numbers)

numbers_as_list = []

for sym in numbers_as_string:
    number = int(sym)
    numbers_as_list.append(number)

sorted_list = sorted(numbers_as_list)

sorted_as_string = list(map(str, sorted_list))[::-1]

print("".join(sorted_as_string))
