import sys

def main():
	for arg in sys.argv:
		if arg != 'cat2.py':
			filename = arg
			#print(filename)
			file = open(filename, "r")
			content = file.read()
			print(content)
			file.close()
if __name__ == '__main__':
	main()