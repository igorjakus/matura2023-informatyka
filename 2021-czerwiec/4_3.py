def czy_palindrom(string):
    return string == string[::-1]


napis = []
with open('napisy.txt', 'r') as file:
    for line in file:
        wiersz = line.strip()

        # 51 znakow -> 26 znak jest środkowy -> 25 indeks
        if czy_palindrom(wiersz + wiersz[0]):
            srodkowy = str(wiersz + wiersz[0])[25]
            napis.append(srodkowy)

        elif czy_palindrom(wiersz[-1] + wiersz):
            srodkowy = str(wiersz[-1] + wiersz)[25]
            napis.append(srodkowy)


print(''.join(napis))
