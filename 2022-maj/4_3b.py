def dobra_trojka(x, y, z):
    if x != y and x != z and y != z:
        if y % x == 0:
            if z % y == 0:
                return True
    return False

def dobra_piatka(a,b,c,d,e):
    if a != b and a != c and a != d and a != e:
        if b != c and b != d and b != e:
            if c != d and c != e:
                if d != e:
                    if e % d == 0 and d % c == 0 and c % b == 0 and b % a == 0:
                        return True
    return False

# test
# print(dobra_piatka(2,6,12,24,48))
# print(dobra_piatka(2,10,12,24,36))


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
print(wielokrotnosci)

count = 0
for x in liczby:
    for y in wielokrotnosci[x]:
        for z in wielokrotnosci[y]:
            for q in wielokrotnosci[z]:
                for v in wielokrotnosci[q]:
                    count += 1
                    print(x, y, z, q, v)

print('wynik', count)
