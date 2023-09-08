def wez_cyfry(string):
    return [c for c in string if c.isdigit()]


kod = []
with open('napisy.txt', 'r') as file:
    for line in file:
        cyfry = [c for c in line.strip() if c.isdigit()]
        if len(cyfry) % 2 == 1:
            cyfry.pop(-1)
        while cyfry:
            liczba = int(cyfry.pop(0) + cyfry.pop(0))
            if liczba in range(65, 91):
                kod.append(chr(liczba))

print(''.join(kod))

licznik = 0
for i, znak in enumerate(kod):
    if znak == 'X':
        licznik += 1
        if licznik == 3:
            print(''.join(kod[:i-2]))
            break
    else:
        licznik = 0