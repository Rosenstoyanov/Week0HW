def prime_factorization(n):
    primeList = []

    for divisor in range(2, n + 1):
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor

            if n % divisor != 0:
                a = (divisor, count)
                primeList.append(a)

    return primeList
