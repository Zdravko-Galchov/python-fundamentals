word = input()

result = ""

for index in range(len(word) - 1, -1, -1):
    result += word[index]

print(result)
