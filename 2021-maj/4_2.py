with open('instrukcje.txt', 'r') as file:
    instrukcja = max_instrukcja = file.readline().split(' ')[0]
    ciag = max_ciag = 1

    for line in file:
        if line.split(' ')[0] == instrukcja:
            ciag += 1
            if ciag > max_ciag:
                max_ciag = ciag
                max_instrukcja = instrukcja
        else:
            instrukcja = line.split(' ')[0]
            ciag = 1


print(max_instrukcja, max_ciag)
