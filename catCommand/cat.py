import sys

def main():
	filename = sys.argv[1]
	print(filename)
	file = open(filename, "r")
	content = file.read()
	print(content)
	file.close()
if __name__ == '__main__':
	main()