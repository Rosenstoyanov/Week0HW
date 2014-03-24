import sys

def main():
    file = open(sys.argv[1], 'r')
    content = file.read()
    a = content.split(' ')
    c = map(int, a)
    print (sum(list(c)))
    file.close()

if __name__ == '__main__':
main()
