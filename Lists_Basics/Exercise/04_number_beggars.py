items_list = input().split(", ")
beggars_count = int(input())

total_sum_per_beggar = []

collected = 0

for beggar in range(beggars_count):
    beggar_index = beggar

    for idx in range(len(items_list)):

        # Check whether the beggar goes out of the possible range. If it does, it's next beggar's turn
        if beggar_index > len(items_list) - 1:
            break

        # Give the item to the beggar according to his turn
        item_value = int(items_list[beggar_index])
        collected += item_value

        # Increase the beggar's index to calculate his next turn after the rest of them
        beggar_index += beggars_count

    total_sum_per_beggar.append(collected)
    collected = 0

print(total_sum_per_beggar)
