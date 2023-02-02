first = int(input())
second = int(input())

a, b = first, second

print(f"Before:\n"
      f"a = {a}\n"
      f"b = {b}")

a, b = second, first

print(f"After:\n"
      f"a = {a}\n"
      f"b = {b}")
