def is_prime(n):
    #deli se na sebe si i na 1
    sum = 0
    for x in range(1,n + 1):
        if n % x == 0:
            sum += x
    if sum == n + 1:
        return True
    else:
        return False
