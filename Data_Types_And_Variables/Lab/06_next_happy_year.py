year = int(input())
year += 1
year_as_string = str(year)

while not len(year_as_string) == len(set(year_as_string)):
    year += 1
    year_as_string = str(year)

print(year)
