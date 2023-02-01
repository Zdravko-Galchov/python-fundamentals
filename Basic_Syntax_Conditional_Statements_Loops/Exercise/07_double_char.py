command = input()

while not command == "End":
    if not command == "SoftUni":
        for ch in command:
            print(ch * 2, end="")
        print()

    command = input()
