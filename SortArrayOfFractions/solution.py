def swap(i,j):
    i,j = j,i
    return i,j
def sort_fractions(fractions):
	#result = 0
	lenFrac = len(fractions)
	for x1 in range(lenFrac):
		currentElem = fractions[x1][0] / fractions[x1][1]
		for x2 in range(lenFrac):
			checkElem = fractions[x2][0] / fractions[x2][1]
			if currentElem < checkElem:
				temp = fractions[x2]
				fractions[x2] = fractions[x1]
				fractions[x1] = temp
	for item in fractions:
		print(item)
#ZSHELL
