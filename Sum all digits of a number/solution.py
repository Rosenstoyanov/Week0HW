def sum_of_digits_n(numb):
    sum = 0
    while numb > 0:
        sum += numb % 10
        numb //= numb
    return sum
