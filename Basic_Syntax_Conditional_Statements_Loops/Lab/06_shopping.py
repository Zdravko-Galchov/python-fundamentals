budget = int(input())

command = input()

while not command == "End":
    product_price = int(command)

    if budget - product_price < 0:
        print("You went in overdraft!")
        exit()

    budget -= product_price

    command = input()

else:
    print("You bought everything needed.")
