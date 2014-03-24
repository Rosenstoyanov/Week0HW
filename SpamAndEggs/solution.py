def prepare_meal(number):
	n = 0
	returnArr = []
	while n <= number:
		if pow(3,n) == number:
			for x in range(1,n):
				returnArr.append('spam')
		n+=1
	if number % 5 == 0:
		returnArr.append('and eggs')
	return " ".join(returnArr)
