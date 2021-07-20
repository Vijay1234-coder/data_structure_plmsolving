
''''''
'''Given a number n, write an efficient function to print all prime factors of n. For example,
if the input number is 12, then output should be “2 2 3”. And if the input number is 315,
then output should be “3 3 5 7”.'''

from math import sqrt


def primeFactor(n):   #      if n=46
    root = int(sqrt(n))     # root = 6

    for div in range(2,root+1):
        while n % div ==0:  # if n becomes 23 then what : in hcf we keep dividing till we reach 1 let say after all posible divsion if

            print(div) # if did'n reach 1 then return number last left and this is edge case n!=1 return number itself
            n = n//div
    if n != 1:   # this is edge case if n is not divisible  we use this when n becomes 23
        print(n)



print(primeFactor(23))