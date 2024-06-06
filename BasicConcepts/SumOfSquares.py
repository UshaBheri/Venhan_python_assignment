def sumOfSquares(list_n):
    total = 0
    for i in list_n:
        total += i ** 2
    return total

list_n = [1,2,3,4,5]
print(sumOfSquares(list_n)) # output: 55