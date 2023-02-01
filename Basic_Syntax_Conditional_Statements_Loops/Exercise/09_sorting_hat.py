command = input()

while not command == "Welcome!":
    student_name = command

    if command == "Voldemort":
        print("You must not speak of that name!")
        exit()

    if len(student_name) < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif len(student_name) == 5:
        print(f"{student_name} goes to Slytherin.")
    elif len(student_name) == 6:
        print(f"{student_name} goes to Ravenclaw.")
    elif len(student_name) > 6:
        print(f"{student_name} goes to Hufflepuff.")

    command = input()

print("Welcome to Hogwarts.")
