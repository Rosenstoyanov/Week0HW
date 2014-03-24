import sys, random

def main():
    filename = sys.argv[1]
    n = int(sys.argv[2])
    file = open(filename, 'w')

    for x in range(0, n):
        l = str(random.randint(1, 1000)) + " "
        file.write(l)
    file.close()

if __name__ == '__main__':
    main()
