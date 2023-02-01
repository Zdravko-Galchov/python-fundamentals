n = int(input())

highest_value = 0
result = ""

for i in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = (weight // time) ** quality

    if snowball_value > highest_value:
        highest_value = snowball_value
        result = f"{weight} : {time} = {snowball_value} ({quality})"

print(result)
