import math

number_of_people = int(input())
lift_capacity = int(input())

result = math.ceil(number_of_people / lift_capacity)

print(result)
