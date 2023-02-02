def glebokosc(string):
    lst = []
    value = 0
    for c in string:
        if c == '[': 
            value += 1
        elif c == ']': 
            lst.append(value)
            value -= 1
    return max(lst)


lista = []
with open('DANE/dane2_3.txt') as file:
    for line in file:
        lista.append(glebokosc(line))


with open('zadanie2_3.txt', 'w') as file:
    for wiersz in lista:
        file.write(str(wiersz) + '\n')