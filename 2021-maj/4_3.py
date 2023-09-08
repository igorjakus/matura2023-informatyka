from collections import Counter


arguments_list = []
with open('instrukcje.txt', 'r') as file:
    for line in file:
        command, argument = line.split(' ')
        if command == "DOPISZ":
            arguments_list.append(argument.strip())


print(Counter(arguments_list).most_common(1))
