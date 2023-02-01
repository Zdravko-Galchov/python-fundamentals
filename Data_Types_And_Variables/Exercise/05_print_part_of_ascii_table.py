start_idx = int(input())
end_idx = int(input())

for idx in range(start_idx, end_idx + 1):
    char = chr(idx)
    print(char, end=" ")
