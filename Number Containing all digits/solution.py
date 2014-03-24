def contains_digits(number, digits):
	exist = False
	numberStr = str(number)
	for item in digits:
		for strItem in numberStr:
			#print(strItem)
			#print(type(item))
			#print (type(strItem))
			if strItem == str(item):
				exist = True
		if exist == False:
			return False
		exist = False
	return True
#ctrl c stop proces
