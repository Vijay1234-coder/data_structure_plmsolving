''' Coin Change Problem Maximum Number of ways
Given a value N, if we want to make change for N cents,
 and we have infinite supply of each of S = { S1, S2, .. , Sm}
 valued coins, how many ways can we make the change?
 The order of coins doesn’t matter.
Example:
for N = 4 and S = {1,2,3},
there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
 So output should be 4.'''   # we can interpret this problem into subset Sum count but difference only is here repetition possible



def coinChange(arr,sum1):
    n=len(arr)
    t= [[0 for j in range(sum1+1)] for i in range(n+1)]

    for i in range(0,n+1):
        t[i][0]=1
    for j in range(1,sum1+1):
        t[0][j]= 0

    for i in range(1,n+1):
        for j in range(1,sum1+1):
            if(arr[i-1]<=j):
                t[i][j] =  t[i][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum1]



print(coinChange([1,2],5))