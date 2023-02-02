key = int(input())
n = int(input())

decrypted_message = ""

for _ in range(n):
    symbol = input()
    transform_symbol = ord(symbol) + key
    new_symbol = chr(transform_symbol)
    decrypted_message += new_symbol

print(decrypted_message)
