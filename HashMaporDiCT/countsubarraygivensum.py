''' given a array find the number of SubArray having sum equal to k'''

def SubarrCount(arr,k):
    sum1 = 0
    count = 0

    dict1={0:1} # sum1=0 starting sum is zero and its count is 1
    for i in range(len(arr)):

        sum1 += arr[i]
        if (sum1-k) in dict1:
            count += dict1.get(sum1-k)
        if sum1 in dict1:
            dict1[sum1] += 1
        else:
            dict1[sum1] = 1
    return count


print(SubarrCount([3,9,-2,4,1,-7,2,6,-5,8,-3,-7,6,2,1],5))





