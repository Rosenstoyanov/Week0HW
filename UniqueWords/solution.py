def unique_words_count(arr):
	countWords = 0
	dicCheck = {}
	for item in arr:
		if item  not in dicCheck:
			dicCheck[item] = 1
		else : 
			dicCheck[item] += 1
	for item in dicCheck:
		countWords += 1
	return countWords

def main():
	print(unique_words_count(["apple", "banana", "apple", "pie"]))
	#print(unique_words_count(["python", "python", "python", "ruby"]))
if __name__ == '__main__':
	main()
