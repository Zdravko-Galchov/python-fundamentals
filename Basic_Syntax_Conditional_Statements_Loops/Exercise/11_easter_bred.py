budget = float(input())
kg_flour_price = float(input())

pack_eggs_price = kg_flour_price * 0.75
liter_milk_price = kg_flour_price * 0.25 + kg_flour_price
milk_needed_price = liter_milk_price / 4

bread_price = kg_flour_price + pack_eggs_price + milk_needed_price

current_breads_count = 0
coloured_eggs = 0

while budget >= bread_price:
    current_breads_count += 1
    budget -= bread_price
    coloured_eggs += 3

    if current_breads_count > 1 and current_breads_count % 3 == 0:
        coloured_eggs -= current_breads_count - 2

print(f"You made {current_breads_count} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
