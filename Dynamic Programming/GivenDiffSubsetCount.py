'''  Count number of subsets of Given difference
     arr:[1,1,2,3]
     diff: 1                                            '''

def outPut(arr,diff):
    sum1  = (diff+sum(arr))//2

    return subsetCount(arr, sum1)





def subsetCount(arr,sum1):

    n = len(arr)

    t = [[0 for j in range(sum1+1)] for i in range(n+1)]
    for i in range(0, n+1):
        t[i][0] = 1
    for j in range(1, sum1+1):
        t[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, sum1+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][sum1]







print(outPut([1,1,1,1,1],3))