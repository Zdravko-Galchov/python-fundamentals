"""
Not optimized, but working
"""

n = int(input())

brackets = ""

for _ in range(n):
    symbol = input()

    if symbol == "(":
        if brackets == "":
            brackets += symbol
        elif brackets[-1] == "(":
            print("UNBALANCED")
            exit()
        else:
            brackets += symbol
    elif symbol == ")":
        if brackets == "":
            print("UNBALANCED")
            exit()
        brackets += symbol

if brackets[-1] == "(":
    print("UNBALANCED")
else:
    print("BALANCED")
