'''Question'''

'''  Given a set of non-negative integers, and a value sum,
     determine if there is a subset of the given set with sum equal to given sum.
     Example:  
 
Input:   set[] = {3, 34, 4, 12, 5, 2},  sum = 9
Output:  True   // There is a subset (4, 5) with sum 9  '''

def SubsetSum(arr,sum1):
    n =  len(arr)
    t = [[False for j in range(sum1+1)] for i in range(n+1)]

    for i in range(n + 1):
        t[i][0] = True
    for i in range(1, sum1 + 1):
        t[0][i] = False

    for i in range(1, n+1):
        for j in range(1, sum1+1):

            if arr[i-1] <= j:
                t[i][j]= t[i-1][j-arr[i-1]] or t[i-1][j]

            else:
                t[i][j]=t[i-1][j]

    return t[n][sum1]






print(SubsetSum([3, 34, 4, 12, 5, 2],9))