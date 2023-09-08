count = 0
szukane_liczby = []
with open('liczby.txt', 'r') as file:
    for line in file:
        liczba = line.strip()
        if liczba[0] == liczba[-1]:
            count += 1
            szukane_liczby.append(int(liczba))


print(count, szukane_liczby[0])