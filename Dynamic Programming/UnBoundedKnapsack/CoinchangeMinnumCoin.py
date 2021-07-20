'''Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm}
valued coins, what is the minimum number of coins to make the change? If it’s not possible to make change, print -1.

Examples:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents'''

import sys

max_int = sys.maxsize

def minCoins(coins,v):
    n=len(coins)
    t=[[0 for j in range(v+1)] for i in range(n+1)]

    for i in range(1,n+1):
        t[i][0]=0
    for j in range(0,v+1):
        t[0][j]= max_int      # if any not define things come then in dp we take int_max
    #also needed to initialize row 2 (i==1)

    for j in range(1,v+1):
        if j%coins[0]==0:
            t[1][j]=j//coins[0]
        else:
            t[1][j]= max_int
    for i in range(2,n+1):
        for j in range(1,v+1):
            if coins[i-1]<=j:
                t[i][j]=min(1+t[i][j-coins[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    if t[n][v]== max_int:
        return -1
    else:
        return t[n][v]





print(minCoins([25, 10, 5],30))
