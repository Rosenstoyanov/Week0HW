def contains_digit(number, digit):
	while number > 0:
		if number % 10 == digit:
			return True
		else:
			number//10
		return False

def main():
	print(contains_digit(123,4))
	print(contains_digit(42,2))
	print(contains_digit(1000,0))
	print(contains_digit(123456789,5))
if __name__ == '__main__':
	main()
