messages_amount = int(input())

for _ in range(messages_amount):
    number = int(input())

    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print("GREAT!")
    else:
        print("Bye.")
