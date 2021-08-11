''' '''
''' Given an array of n elements and a number m we need to find all the distinct pair existing in the array
 whose pair sum
is divisible by given number m
print total number  of such pairs.Distinct pairs means (1,2) and
(2,1) are same ie ordering of the pairs doesn't matter.

input: 10,9,4,5,7,2,8,20,21      m: 15 '''

'''solution in O(n**2)'''

'''it will not pass all the test cases because  distict  pair not follow'''


# def PairSumCount(arr,m):
#     count=0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if(arr[i]+arr[j]) % m== 0:
#                 count+=1
#     return count
#
#
#
# print(PairSumCount([10,9,4,10,7,2,10,20,21],15))

def PairSumCount(arr,m):
    dict1 = {}
    count = 0
    for num in arr:
        if num % m in dict1:
            dict1[num % m] += 1
        else:
            dict1[num % m] = 1  # { 10:1,9:1,4:1,7:1,2:1,0:2,5:1,6:1}

    for rem in dict1:
        complement = m - rem
        pairs = 0
        if complement ==  m or (2 * complement == m): # complement==m means rem==0
            pairs = (dict1[rem] * (dict1[rem] - 1)) // 2
        elif (complement in dict1):
            pairs = dict1[rem] * dict1[complement]
            dict1[rem] = 0
        count += pairs
    return count


print(PairSumCount([10, 9, 4, 7, 2, 15, 30, 20, 21], 15))
