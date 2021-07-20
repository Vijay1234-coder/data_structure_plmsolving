'''

Sum of subset differences
Given a set of integers, the task is to divide it into two sets S1 and S2 such
 that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements,
 Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example:
Input:  arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11 '''

def minimumSubsetSumDiff(arr):
    Min = 1000000000000
    l = []
    Subset_sum_Range = sum(arr)
    n = len(arr)
    t = [[0 for j in range(Subset_sum_Range+1)] for j in range(n+1)]

    for i in range(0, n+1):
        t[i][0] = True
    for j in range(1,Subset_sum_Range):
        t[0][j] = False
    for i in range(1,n+1):
        for j in range(1,Subset_sum_Range):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i - 1][j]
    for j in range(0,Subset_sum_Range//2 +1 ):
        if t[n][j]==True:
            l.append(j)
    for i in range(len(l)):
        Min = min(Min,(Subset_sum_Range-2*l[i]))
    return Min



print(minimumSubsetSumDiff([1, 6, 11, 5]))







