string_one = input()
string_two = input()

result = string_one

for index in range(len(string_one)):
    if not string_one[index] == string_two[index]:
        result = string_two[:index + 1] + string_one[index + 1:]
        print(result)
