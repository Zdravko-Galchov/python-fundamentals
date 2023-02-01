n = int(input())

tank_capacity = 255

current_state = 0

for _ in range(n):
    liters_of_water = int(input())

    if liters_of_water + current_state > tank_capacity:
        print(f"Insufficient capacity!")
    else:
        current_state += liters_of_water

print(current_state)
