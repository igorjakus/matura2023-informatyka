lista = []

with open('liczby.txt', 'r') as file:
    for line in file:
        liczba = int(line.strip())
        lista.append(liczba)

# ile unikatowych
unikat = set(lista)
print(len(unikat))

# ile powtarza się dokładnie dwa razy
licznik = 0
for x in unikat:
    if lista.count(x) == 2:
        licznik += 1
print(licznik)

# ile powtarza się dokładnie trzy razy
licznik = 0
for x in unikat:
    if lista.count(x) == 3:
        licznik += 1
print(licznik)



