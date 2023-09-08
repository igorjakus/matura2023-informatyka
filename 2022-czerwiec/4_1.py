with open('liczby.txt', 'r') as file:
    for line in file:
        odbicie = int(line.strip()[::-1])
        if odbicie % 17 == 0:
            print(odbicie)