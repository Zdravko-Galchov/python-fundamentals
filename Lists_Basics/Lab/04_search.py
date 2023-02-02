n = int(input())

word = input()

strings_list = []

for _ in range(n):
    some_string = input()
    strings_list.append(some_string)

print(strings_list)

filtered_list = []

for el in strings_list:
    if word in el:
        filtered_list.append(el)

print(filtered_list)
