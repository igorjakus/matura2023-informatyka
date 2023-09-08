count = 0
with open('instrukcje.txt', 'r') as file:
    for line in file:
        polecenie = line.split(' ')[0]
        if polecenie == 'DOPISZ':
            count += 1
        elif polecenie == 'USUN':
            count -= 1

print(count)
