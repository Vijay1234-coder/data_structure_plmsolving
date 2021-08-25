'''Q'''
'''We Have to find number of trailing zeros in Factorial of an number'''
'''Best Approach is to find number of 2s and 5s in prime Factorization of factoraial
How to find number of 5s and 2s : if we need to find number of 5s and 2s in n!
just find number of 5 in "n" because number of 5s are less than number of 2s in factorial of number of finding only number of 5s is suuficient
 we also need check if n is containg 25 or 125 or.. not becuase zeros are also due to this only have'''




def trailingZeros(n):
    res =0
    i =5
    while i<=n:
        res +=  n//i
        i = i*5
    return res


print(trailingZeros(100))