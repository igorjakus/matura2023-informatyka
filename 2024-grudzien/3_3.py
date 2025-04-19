def f(x: int):
    maxi = int("".join(sorted(str(x), reverse=True)))
    mini = int("".join(sorted(str(x), reverse=False)))
    return maxi - mini

xs = []
same = 0
greater = 0
less = 0

with open("dane/liczby.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        diff = f(number)
        if number == diff:
            xs.append(number)
            same += 1
        elif diff < number:
            less += 1
        else:
            greater += 1

print("różnica mniejsza od liczby:", less)
print("różnica równa liczbie:", same)
print("różnica większa od liczby:", greater)
for x in xs:
    print(x)