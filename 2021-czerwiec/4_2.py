kod = []
with open('napisy.txt', 'r') as file:
    for i in range(50):
        for _ in range(19):
            file.readline()
        line = file.readline()
        kod.append(line[i])


print(''.join(kod))
