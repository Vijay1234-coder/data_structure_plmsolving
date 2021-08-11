'''1. You are given an array of integers(arr) and a number K.
2. You have to find the count of subarrays whose sum is divisible by K.'''



def SubArrayCount(arr,k):
    sum1 = 0
    count= 0
    dict1={0:1}  # {0: 2, 2: 1, 5: 3, 3: 1, 1: 1}
    for num in arr:
        sum1+=num
        rem = sum1 % k
        if rem<0:    # here this is edge case if rem id negative biut remainder is never neagtive but eg: 7n-5 equivalent to 7n'+2(7n-5+7-7=7(n-1)+2)
            rem = rem + k # kn-y = here remainder is negative (-y) then it is equivalent to kn-y+k-k = k(n-1)+(k-y)


        if  rem in dict1:
            count += dict1.get(rem)

            dict1[rem]+=1

        else:
            dict1[rem]=1
    return count

print(SubArrayCount([2,-6,3,1,2,8,2,1],7))