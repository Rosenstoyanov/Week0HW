import sys

def main():
	operation = sys.argv[1]
	fileName = sys.argv[2]
	file = open(fileName, 'r')
	contents = file.read()
	if operation == "chars":
		chars = 0
		#contents.split("\n")
		#print(contents)
		print(len(contents))
		#chars = contents.count()
	if operation == "words":
		words = 0
		contentsW = contents.split(" ")
		print(len(contentsW))
	if operation == "lines":
		words = 0
		contentsW = contents.split("\n")
		print(len(contentsW))
	file.close()
if __name__ == '__main__':
	main()