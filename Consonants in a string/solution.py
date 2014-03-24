def count_consonants(str):
	coutVlowels = len(str)
	for item in str.lower():
		if item == 'a':
			coutVlowels -= 1
		elif item == 'e':
			coutVlowels -= 1
		elif item == 'i':
			coutVlowels -= 1
		elif item == 'o':
			coutVlowels -= 1
		elif item == 'u':
			coutVlowels -= 1
		elif item == 'y':
			coutVlowels -= 1
	return coutVlowels
