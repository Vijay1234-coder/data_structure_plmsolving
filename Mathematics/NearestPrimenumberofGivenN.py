from math import sqrt

n =25

def find_nearest(prime,n):
    start =0
    end = len(prime)-1
    floor = 0
    ceil  =0
    while start<=end:
        mid =(start+end)//2
        if prime[mid]==n:
            return prime[mid]
        elif prime[mid]>n:
            ceil = prime[mid]
            end = mid-1
        else:
            floor=prime[mid]
            start =mid+1
    x1 =ceil-n
    x2 = n -floor
    if x1==x2:
        print(floor,ceil)
    else:
        Min = min(x1,x2)
        if Min == x1:
            print(ceil)

        else:
            print(floor)













def is_prime(n):
    root =int(sqrt(n))
    if n<=1:
        return False
    if n==3 or n==2:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(2,root+1):
        if n%i==0:
            return False
    return True

prime =[]

def primeprint(n):
    if n<=1:
        print(2)

    for i in range(2,n+5):
        if is_prime(i)==True:
            prime.append(i)

    find_nearest(prime,n)


primeprint(n)