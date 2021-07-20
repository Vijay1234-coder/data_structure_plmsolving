'''binary search'''
'''Count of ways to split an Array into three contiguous Subarrays having increasing Sum
Difficulty Level : Hard
Last Updated : 11 May, 2021
Given an array arr[] consisting of non-negative integers, the task is to find the number of ways to split the array into three non-empty contiguous subarrays such that their respective sum of elements are in increasing order.

Examples:

Input: arr[] = {2, 3, 1, 7} 
Output: 2 
Explanation: 
{{2}, {3, 1}, {7}}, {{2}, {3}, {1, 7}} are the possible splits.
Input: arr[] = {1, 2, 0} 
Output: 0'''


def splitArray(arrm,n):
    count=0
    prefixSum = [0]*n
    prefixSum[0]=arr[0]
    for i in range(1,n):
        prefixSum[i]=prefixSum[i-1]+arr[i]
    total = prefixSum[n-1]
    print(prefixSum)
    for i in range(1,n-1):
        for j in range(1,n-1):
            left= prefixSum[i]-arr[i]
            right = total-prefixSum[j]
            mid = total - (left+right)

            if left<=mid<=right:
                count+=1
    return count





arr =[2, 3, 1, 7]
n = len(arr)
print(splitArray(arr,n))