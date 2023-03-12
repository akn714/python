def OR(x,y):
    return 1 if (x==1 or y==1) else 0
def AND(x,y):
    return 1 if (x==1 and y==1) else 0
def NOT(x):
    return 0 if x==1 else 1

def NAND(x,y):
    return NOT(AND(x,y))
def NOR(x,y):
    return NOT(OR(x,y))
def XOR(x,y):
    return OR(AND(x,NOT(y)),AND(NOT(x),y))


def ADDER(x,y,z):
    sum = XOR(XOR(x,y),z)
    carry = OR(AND(XOR(x,y),z),AND(x,y))
    return [sum,carry]

def add(arr1,arr2,c):
    arr = [0,0,0,0]
    arr[0] = ADDER(arr1[0],arr2[0],ADDER(arr1[1],arr2[1],ADDER(arr1[2],arr2[2],ADDER(arr1[3],arr2[3],c)[1])[1])[1])[0]
    arr[1] = ADDER(arr1[1],arr2[1],ADDER(arr1[2],arr2[2],ADDER(arr1[3],arr2[3],c)[1])[1])[0]
    arr[2] = ADDER(arr1[2],arr2[2],ADDER(arr1[3],arr2[3],c)[1])[0]
    arr[3] = ADDER(arr1[3],arr2[3],c)[0]
    carry = ADDER(arr1[0],arr2[0],ADDER(arr1[1],arr2[1],ADDER(arr1[2],arr2[2],ADDER(arr1[3],arr2[3],c)[1])[1])[1])[1]
    return [arr,carry]

# addbits is a function to add two binary no.s of n bits using recursion
# this function is not correct and is incomplete as well
# def addbits(arr1,arr2,c,n,count):
#     if count==n:
#         return ADDER(arr1[n],arr2[n],c)
#     return addbits(arr1,arr2,c,n+1,count+1)

print('enter your 4 bit binary numbers: [note: please note that bits should be space seperated]')
while True:
    try:
        print('number 1: ',end="")
        arr1 = list(map(int,input().split()))
        print('number 2: ',end="")
        arr2 = list(map(int,input().split()))
    except Exception as e:
        print('[err : %s]'%e)
    carry = 0
    try:
        print('ans : ',*add(arr1,arr2,carry))
    except Exception as e:
        print('[err : %s]'%e)
