from mathtool import getFactors, getfibonacciSeries

def sumSquare(n):
    sum = 0
    for i in range(1,n+1):
        sum += (i*i)
    print(sum)
# sumSquare(3)

#------------------------------------------------------------------------------------------------

def palindromeNum(n):
    b = bin(n)
    s = str(b[2:])
    for i in range(0,int(len(s)/2)):
        temp = None
        if s[i] == s[len(s)-i-1]:
            temp = True
        else:
            temp = False
            break
    if temp: print("yes")
    else: print("no")
# palindromeNum(5)

#------------------------------------------------------------------------------------------------

def minSum(n):
    sum = 0
    for i in range(2,n):
        if n%i == 0:
            sum += i
        if sum > n:
            sum -= i
            break
    print(sum)
# minSum(10)

#------------------------------------------------------------------------------------------------

def nthFibonacci(n):
    s = getfibonacciSeries(n)
    return s[n-1]
# print(nthFibonacci(5))

#------------------------------------------------------------------------------------------------

def maxNum(a,b):
    if a==b: return "both are equal"
    elif a>b: return a
    else: return b
# print(maxNum(5,4))

#------------------------------------------------------------------------------------------------

def primeNum(a,b):
    for i in range(a,b+1):
        if checker(i): print(i,end=" ")
        else: continue
def checker(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        else: continue
    return True
# primeNum(23,46)

#------------------------------------------------------------------------------------------------

def areaOfCircle(r):
    return 3.14*r*r
# print(areaOfCircle(2))

#------------------------------------------------------------------------------------------------

def checkInFibo(n):
    s = getfibonacciSeries(n)
    if n in s: return "yes"
    else: return "no"
# print(checkInFibo(2))

#------------------------------------------------------------------------------------------------

def cubeSum(n):
    sum = 0
    for i in range(0,n+1):
        sum += (i*i*i)
    return sum
# print(cubeSum(4))

#------------------------------------------------------------------------------------------------

def sumOfOddFactors(n):
    sum = 0
    f = getFactors(n)
    print(f)
    for i in range(0,len(f)):
        if f[i]%2 != 0: sum += f[i]
        else: continue
    return sum
# print(sumOfOddFactors(35))

#------------------------------------------------------------------------------------------------

def sumOfArray(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum += arr[i]
    return sum
# print(sumOfArray([2,3,5,2]))

#------------------------------------------------------------------------------------------------

def checkTriangle(a,b,c):
    if a+b+c != 180: return "this triangle does not exists"
    else:
        # if(a+b>)
        return "yes this triangle exists"
# print(checkTriangle(60,60,60))

#------------------------------------------------------------------------------------------------
from mathtool import getPrimes
def maxPrimeFactor(n):
    maxfactor = 0
    primes = getPrimes(n)
    print(primes)
    for i in primes:
        if n%i == 0: maxfactor = i
    return maxfactor
# print(maxPrimeFactor(20))
