# gives fibonacci series
series = []
counter = 0
def getfibonacciSeries(n):
    a = 0
    b = 1
    series.append(a)
    series.append(b)
    temp(a,b,n)
    return series

def temp(a,b,n):
    c = a+b
    if n==0:
        series.append(c)
        return
    series.append(c)
    temp(b,c,n-1)


# gives factors of a number
factors = []
def getFactors(n):
    for i in range(2,n+1):
        if n%i == 0: factors.append(i)
        else: continue
    return factors


# gives prime numbers
primes = []
def getPrimes(n):
    for i in range(2,n+1):
        if checker(i): primes.append(i)
        else: continue
    return primes
def checker(n):
    for i in range(2,n+1):
        if i==n: continue
        elif n%i != 0: continue
        else: return False
    return True
# print(getPrimes(100))
