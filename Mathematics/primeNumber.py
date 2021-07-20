''' input: n
o/p: prime or not'''
import math

def primeNumber(n):
    count = 0
    root = int(math.sqrt(n))

    if n==1 or n==0:
        return "Not Prime"



    for div in range(2,root+1):
        if n % div ==0:
            count+=1
            break
    if count==0:
        return "Prime"
    else:
        return "Not Prime"


n = int(input("enter number"))
print(primeNumber(n))