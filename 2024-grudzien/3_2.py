def cnt_dzielniki(x: int) -> int:
    ctr = 0
    for i in range(2, x + 1):
        if x % i == 0:
            ctr += 1
            while x % i == 0:
                x //= i
    return ctr

xs = []
with open("dane/liczby.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if cnt_dzielniki(number) >= 5:
            xs.append(number)


for x in xs:
    print(x)