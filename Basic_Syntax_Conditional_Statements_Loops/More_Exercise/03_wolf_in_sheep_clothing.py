animals = input().split(", ")

sheep_counter = 0

for index in range(len(animals) -1, -1, -1):
    if animals[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif animals[index] == "sheep":
        sheep_counter += 1
    if animals[index] == "wolf":
        print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")
        break
