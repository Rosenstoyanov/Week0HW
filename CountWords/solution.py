def count_words(arr):
	dictFruds = {}
	countSuvp = 0
	for item in arr:
		if item  not in dictFruds:
			dictFruds[item] = 1
		else : 
			dictFruds[item] += 1
		"""for checkItem in arr:
			countSuvp = 0
			if item == checkItem:
				countSuvp += 1
				dictFruds{item,countSuvp}
				"""
	return dictFruds

def main():
	print(count_words(["apple", "banana", "apple", "pie"]))
if __name__ == '__main__':
	main()