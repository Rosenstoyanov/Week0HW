def list_to_number(digits):
	lengthN = len(digits) - 1
	returnNumber = 0
	for numb in digits:
		returnNumber += numb*(pow(10,lengthN))
		lengthN -= 1
	return returnNumber
