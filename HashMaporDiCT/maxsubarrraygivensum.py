'''Given: k find the max length of subarray having sum is equal to k
   Note: we can solve this plm in various way if all the given integer will be positive then we can apply sliding Window Algorithm
but parent array is mixture of positive as well as negative numbers than we will solve this using hash map or in python its Dictionarty'''

'''arr: [-5,8,-14,2,4,12]
k =-5
ans : 5  '''

def subArrMax(arr,k):

    Max=0
    sum1=0
    i=-1
    dict1={sum1:i}   #{0:-1}
    for i in range(len(arr)):
        sum1+=arr[i]
        if sum1==k:
            Max=max(Max,i+1)


        if (sum1-k) in dict1:
            Max=max(Max,i-dict1.get(sum1-k))

        dict1[sum1]=i
    return Max





print(subArrMax([3,9,-2,4,1,-7,2,6,-5,8,-3,-7,6,2,1],3))