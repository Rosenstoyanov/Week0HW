def count_vowels(str):
	#str.lower()
	coutVlowels = 0
	for item in str.lower():
		if item == 'a':
			coutVlowels += 1
		if item == 'e':
			coutVlowels += 1
		if item == 'i':
			coutVlowels += 1
		if item == 'o':
			coutVlowels += 1
		if item == 'u':
			coutVlowels += 1
		if item == 'y':
			coutVlowels += 1
	return coutVlowels
