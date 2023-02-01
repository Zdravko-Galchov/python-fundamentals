decorations_qty = int(input())  # You buy every time you go shopping
days_left = int(input())        # Days left until Christmas

budget = 0
spirit_points = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

day = 0

while days_left > 0:
    day += 1
    days_left -= 1

    # Increasing the qty of decorations that have to be bought by 2
    if day % 11 == 0:
        decorations_qty += 2

    # Buy Ornament Set
    if day % 2 == 0:
        budget += ornament_set_price * decorations_qty
        spirit_points += 5

    # Buy Tree Skirts and Tree Garlands
    if day % 3 == 0:
        budget += (tree_skirt_price + tree_garland_price) * decorations_qty
        spirit_points += 13

    # Buy Tree Lights
    if day % 5 == 0:
        budget += tree_lights_price * decorations_qty
        spirit_points += 17

        if day % 3 == 0:
            spirit_points += 30

    # Cat ruins everything
    if day % 10 == 0:
        spirit_points -= 20
        budget += tree_skirt_price + tree_garland_price + tree_lights_price

    # Cat ruins absolutely everything
    if day % 10 == 0 and days_left == 0:
        spirit_points -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_points}")
