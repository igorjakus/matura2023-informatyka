def is_prime(n):
    if n == 2 or n == 3:
        return True

    if n <= 1 or n % 2 == 0:
        return False

    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True


with open('liczby.txt', 'r') as file:
    for line in file:
        liczba = int(line.strip())
        odbicie = int(line.strip()[::-1])

        if is_prime(liczba) and is_prime(odbicie):
            print(liczba)
