def magic_square(matrix):
    matrix_len = len(matrix)
    sum1 = 0
    sum2 = 0
    #print(matrix_len)
    for x in range(0, matrix_len):
        sum1 += matrix[0][x]
    #print(row_one_sum)

    for x in range(0, matrix_len):
        for y in range(0, matrix_len):
            sum2 += matrix[x][y]
        if sum1 != sum2:
            return False
        else:
            sum2 = 0
    print(sum2)
    for x in range(0, matrix_len):
        for y in range(0, matrix_len):
            sum2 += matrix[y][x]
        if sum1 != sum2:
            return False
        else:
            sum2 = 0

    for x in range(0, matrix_len):
        for y in range(0, matrix_len):
            if x == y:
                sum2 += matrix[x][y]
    if sum1 != sum2:
        return False
    else:
        sum2 = 0

    for x in range(0, matrix_len):
        for y in range(0, matrix_len):
            if x + y == matrix_len - 1:
                sum2 += matrix[x][y]
    if sum1 != sum2:
        return False
    else:
        sum2 = 0
        return True

def main():
    print(magic_square([[1,2,3], [4,5,6], [7,8,9]]))
if __name__ == '__main__':
    main()
