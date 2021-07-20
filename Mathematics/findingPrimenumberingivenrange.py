
'''find prime number till that range inclusive'''
import math

def primeNumber(n):
    count = 0
    root = int(math.sqrt(n))

    if n==1 or n==0:
        return False



    for div in range(2,root+1):
        if n % div ==0:
            count+=1
            break
    if count==0:
        return True
    else:
        return False

def findPrime(n):
    arr = []
    for i in range(2,n+1):
        if primeNumber(i)==True:
            arr.append(i)
    return arr








print(findPrime(25))
# ans : 2,3,5 ,7,11,13,17,19,23