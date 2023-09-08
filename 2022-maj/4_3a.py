def dobra_trojka(x, y, z):
    if x != y and x != z and y != z:
        if y % x == 0:
            if z % y == 0:
                return True
    return False

# test
# print(dobra_trojka(2,6,12))
# print(dobra_trojka(2,10,12))


liczby = []
with open('liczby.txt', 'r') as file:
    for line in file:
        liczby.append(int(line))

liczby.sort()
#print(liczby)

wielokrotnosci = {}
for i, x in enumerate(liczby):
    podzielne = []
    for y in liczby[i+1:]:
        if y % x == 0:
            podzielne.append(y)
    wielokrotnosci[x] = podzielne
#print(wielokrotnosci)

count = 0
for x in liczby:
    for y in wielokrotnosci[x]:
        for z in wielokrotnosci[y]:
            count += 1
            print(x, y, z)

print('wynik', count)
