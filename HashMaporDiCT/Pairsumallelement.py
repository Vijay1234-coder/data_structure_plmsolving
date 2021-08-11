'''1. You are given an array(arr) of integers and a number K.
   2. You have to find if the given array can be divided into pairs such that the sum of every pair is divisible by k. return True else return False '''


def PairDivisible(arr,m):
    dict1 = {}
    result = True
    for num in arr:
        if num % m not in dict1:
            dict1[num % m] = 1
        else:
            dict1[num % m] += 1
    print(dict1)

    for rem in dict1:
        complement= m - rem

        if rem == 0 or 2 * rem == m:
            if dict1[rem] % 2 != 0:
                result=False
                return result
        elif complement in dict1:
            if dict1[complement]!=dict1[rem]:
                result=False
        elif complement not in dict1:
            result=False

    return result

print(PairDivisible([56,22,34,12,78,98,69,1],10))















