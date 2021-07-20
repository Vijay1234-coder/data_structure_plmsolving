''''''
'''The task is to find the length of the longest subsequence in a given array of integers such that all elements of the 
subsequence are sorted in strictly ascending order. This is called the Longest Increasing Subsequence (LIS) problem.

For example, the length of the LIS for[15,27,14,38,26,55,46,65,85]  is 6  since the longest increasing subsequence is
[15,27,38,55,65,85]'''

arr = [15,27,14,38,26,55,46,65,85]
n =len(arr)
lis =[]
for i in range(n):
    for j in range(1,n):
        if arr[i]<=arr[j]:
            lis.append(arr[i])



