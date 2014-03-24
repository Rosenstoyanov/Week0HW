def is_number_balanced(n):
	strNumb = str(n)
	Lsum = 0
	Rsum = 0
	numbLen = len(strNumb)
	if numbLen == 1 :
		return True
	if numbLen % 2 == 0 :
		for x in range(0,numbLen/2):
			Lsum += int(strNumb[x])
		for x in range(numbLen/2,numbLen):
			Rsum += int(strNumb[x])
		return Rsum == Lsum
	else :
		for x in range(0,numbLen//2):
			Lsum += int(strNumb[x])
		for x in range(numbLen//2 + 1,numbLen):
			Rsum += int(strNumb[x])
		return Rsum == Lsum
