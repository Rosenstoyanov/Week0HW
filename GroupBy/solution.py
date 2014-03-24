def groupby(func, seq):
	#lambda x : x%2 vzema x i vru6ta x % 2 
	dictToReturn = {}
	for item in seq:
		if func(item) in dictToReturn:
			dictToReturn[func(item)].append(item)
		else:
			dictToReturn[func(item)] = [item]
	return dictToReturn
def main():
	print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
if __name__ == '__main__':
	main()