import sys

def main():
	for arg in sys.argv:
		if arg != "concat_files.py":
			fileName = "MEGATRON.txt"
			file = open(arg, 'r')
			contents = file.read()
			file.close()
			file = open(fileName, 'a+')
			file.write(contents)
			file.write("\n")
			file.close()
if __name__ == '__main__':
	main()