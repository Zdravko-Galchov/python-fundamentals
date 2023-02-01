command = input()

coffees_needed = 0

while not command == "END":
    check_command = command.lower()
    if check_command == "coding":
        if command.islower():
            coffees_needed += 1
        else:
            coffees_needed += 2
    elif check_command == "dog":
        if command.islower():
            coffees_needed += 1
        else:
            coffees_needed += 2
    elif check_command == "cat":
        if command.islower():
            coffees_needed += 1
        else:
            coffees_needed += 2
    elif check_command == "movie":
        if command.islower():
            coffees_needed += 1
        else:
            coffees_needed += 2

    command = input()

if coffees_needed > 5:
    print("You need extra sleep")
else:
    print(coffees_needed)
