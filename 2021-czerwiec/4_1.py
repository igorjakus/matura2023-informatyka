def ile_cyfr(string):
    return sum(1 for c in string if c.isdigit())


counter = 0
with open('napisy.txt', 'r') as file:
    for line in file:
        counter += ile_cyfr(line)


print(counter)
