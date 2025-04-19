from math import sqrt

xs = []
with open("dane/liczby.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        sq = int(sqrt(number))
        if sq * sq == number:
            xs.append(number)


print(len(xs), xs[0])