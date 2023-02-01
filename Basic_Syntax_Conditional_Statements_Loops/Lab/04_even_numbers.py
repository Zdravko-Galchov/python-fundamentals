n = int(input())

for _ in range(n):
    number = int(input())

    if not number % 2 == 0:
        print(f"{number} is odd!")
        exit()

print("All numbers are even.")
