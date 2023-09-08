# generuj sito eratostenesa od 0 do n włącznie (ulatwienie z indeksami)
# mozemy generowac od 0 do sqrt(n) ale chyba nie ma potrzeby
def generuj_sito(n):
    array = [1 for i in range(0, n+1)]

    # 0 i 1 nie są pierwsze
    array[0] = 0
    array[1] = 0

    # wielokrotnosci 2 nie są pierwsze
    for j in range(2*2, n+1, 2):
        array[j] = 0

    # wielokrotnosci kolejnych liczb nie są pierwsze
    for j in range(3, n+1, 2):
        for k in range(j*j, n+1, j):
            array[k] = 0

    zbior_pierwszych = set()
    for i, x in enumerate(array):
        if x == 1:
            zbior_pierwszych.add(i)

    # print(zbior_pierwszych)
    return zbior_pierwszych


def czynniki_pierwsze(x):
    licznik = 0
    pierwsze = generuj_sito(x)
    for pierwsza in pierwsze:
        if x % pierwsza == 0:
            while x % pierwsza == 0:
                licznik += 1
                x = x//pierwsza
    return licznik


def rozne_czynniki_pierwsze(x):
    licznik = 0
    pierwsze = generuj_sito(x)
    for pierwsza in pierwsze:
        if x % pierwsza == 0:
            licznik += 1
            x = x//pierwsza
    return licznik

liczby = []
with open('liczby.txt', 'r') as file:
    for line in file:
        liczby.append(int(line))


czynniki = []
rozne_czynniki = []

for liczba in liczby:
    czynniki.append( (czynniki_pierwsze(liczba), liczba) )
    rozne_czynniki.append( (rozne_czynniki_pierwsze(liczba), liczba) )


print(max(czynniki))
print(max(rozne_czynniki))
