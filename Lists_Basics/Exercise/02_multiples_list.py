factor = int(input())
count = int(input())

multiples_list = []

current_number = factor

while len(multiples_list) < count:
    if current_number % factor == 0:
        multiples_list.append(current_number)

    current_number += 1

print(multiples_list)
