numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 0
f = n ** (1 / 2)
    for a in range(2, int(f + 1)):
        if n % a == 0:
            is_prime = False
            break