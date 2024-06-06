def primeNumber(n):
    factors = 0
    for i in range(2,n):
        if(n%i == 0):
            factors += 1
    if(factors > 1):
        return "Prime Number"
    else:
        return "Not a Prime Number"

n = 7
print(primeNumber(n)) # output: Not a Prime Number


