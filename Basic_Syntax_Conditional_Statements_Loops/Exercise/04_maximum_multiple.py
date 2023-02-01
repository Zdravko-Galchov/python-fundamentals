divisor = int(input())   # A positive number
boundary = int(input())  # A positive number

result = 0

for num in range(boundary + 1):
    if num % divisor == 0:
        result = num

print(result)
