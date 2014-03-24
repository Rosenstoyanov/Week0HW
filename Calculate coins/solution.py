def calculate_coins(param):
    coinList = [100, 50, 20, 10, 5, 2, 1]
    sum = int(round(param * 100))
    result = dict()
    for item in coinList:
        result[item] = sum // item
        sum -= result[item] * item
    return result
