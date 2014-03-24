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
def prime_number_of_divisors(n):
	sum = 0
	for x in range(1,n + 1):
		if n % x == 0:
			sum += 1
	return is_prime(sum)

def main():
	print(prime_number_of_divisors(7))
	print(prime_number_of_divisors(8))
	print(prime_number_of_divisors(9))
if __name__ == '__main__':
	main()
