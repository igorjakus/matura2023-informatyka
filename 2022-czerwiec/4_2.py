wartosci = []

with open('liczby.txt', 'r') as file:
    for line in file:
        liczba = int(line.strip())
        odbicie = int(line.strip()[::-1])
        modul = abs(liczba - odbicie)
        wartosci.append((modul, liczba))

print(wartosci)
max_modul, max_liczba = max(wartosci)
print(max_liczba, max_modul)
