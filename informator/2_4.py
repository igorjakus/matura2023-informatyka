odpowiedzi = []
def czy_poprawne(wyrazenie):
    l = 0
    p = 0
    for c in wyrazenie:
        if c == '[':
            l += 1
        if c == ']':
            p += 1

        if p > l:
            return False

    if l == p:
        return True
    
    return False

with open('DANE/dane2_4.txt') as file:
    for line in file:
        odpowiedzi.append(czy_poprawne(line))


with open('zadanie2_4.txt', 'w') as file:
    for odpowiedz in odpowiedzi:
        if odpowiedz:
            file.write('tak\n')
        else:
            file.write('nie\n')

