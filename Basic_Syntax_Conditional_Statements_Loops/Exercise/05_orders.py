orders_count = int(input())

total_price = 0

for order in range(orders_count):
    price_per_capsule = float(input())
    day = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue

    if day < 1 or day > 31:
        continue

    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    coffee_price = capsules_per_day * price_per_capsule * day

    total_price += coffee_price

    print(f"The price for the coffee is: ${coffee_price:.2f}")

print(f"Total: ${total_price:.2f}")
