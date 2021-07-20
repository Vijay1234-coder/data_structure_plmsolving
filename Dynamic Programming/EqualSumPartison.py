''''''
''' Partition problem is to determine whether a given set can be partitioned into two subsets such that the
     sum of elements
    in both subsets is the same.

Examples:

arr[] = {1, 5, 11, 5}
Output: true
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false
The array cannot be partitioned into equal sum sets.'''

def equalSumPartition(arr,n):  # This function Will return True if  subset exist false if not
    sum1=0


    for i in range(n):
        sum1+=arr[i]
    if sum1%2 !=0:
        return False
    else:
        sum1 = int(sum1*0.5)

        t = [[False for j in range(sum1+1)]for i in range(n+1)]

        for i in range(0,n+1):
            t[i][0] = True
        for j in range(1,sum1+1):
            t[0][j]= False

        for i in range(1,n+1):
            for j in range(1,sum1+1):
                if arr[i-1] <= j:
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]

                else:
                    t[i][j] = t[i-1][j]
        # return t[n][sum1]

        # return t[n][sum1]
        set1, set2 = [], []
        if (t[n][sum1]!=True):
            return False

        i = n
        currSum = sum1
        while (i > 0 and currSum >= 0):
            if (t[i - 1][currSum]):
                i -= 1
                set2.append(arr[i])


            elif (t[i - 1][currSum - arr[i - 1]]):
                i -= 1
                currSum -= arr[i]
                set1.append(arr[i])

        return set1 ,set2











arr=[1,5,11,5]
n=len(arr)
print(equalSumPartition(arr,n))
#

