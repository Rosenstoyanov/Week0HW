def is_an_bn(word):
	wordL = len(str(word))
	if word == "":
		return True
	else:
		if wordL % 2 == 0:
			first = word[ : int(wordL / 2)]
			second = word[int(wordL / 2) : ]
			for item in first:
				if item != 'a':
					return False
			for item in second:
				if item != 'b':
					return False
			return True
		else:
			return False


def main():
	print(is_an_bn(""))
	print(is_an_bn("aaaaabbbbb"))
	print(is_an_bn("rado"))
if __name__ == '__main__':
	main()