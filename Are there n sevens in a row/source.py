def sevens_in_a_row(arr, n):
	numberOfItems = 0
	for item in arr:
		if item == 7:
			numberOfItems+=1
	if numberOfItems >= n:
		return True
	else :
		return False
