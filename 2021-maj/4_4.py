napis = []
with open('instrukcje.txt', 'r') as file:
    for line in file:
        command, value = line.strip().split(' ')
        if command == "DOPISZ":
            napis.append(value)
        elif command == "USUN":
            napis.pop()
        elif command == "ZMIEN":
            napis[-1] = value
        elif command == "PRZESUN":
            index = napis.index(value)
            if napis[index] == 'Z':
                napis[index] = 'A'
            else:
                napis[index] = chr(ord(napis[index]) + 1)


print(''.join(napis))
