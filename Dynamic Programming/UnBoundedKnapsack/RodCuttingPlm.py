'''Rod Cutting Problem
 Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
  Determine the  maximum value obtainable by cutting up the rod and selling the pieces.
Example:
if length of the rod is 8 and the values of different pieces are given as following,
 then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

length = 8 '''

def rodCutProfit(larr,price,n,length):

    t =[[0 for j in range(length+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(length+1):
            if (i==0 or j==0):
                t[i][j]=0
            if larr[i-1]<=j:
                t[i][j] = max(price[i-1]+t[i][j-larr[i-1]],t[i-1][j])

            else:
                t[i][j] = t[i-1][j]

    return t[n][length]



larr=[1,2,3,4,5,6,7,8]
price=[1,5,8,9,10,17,17,20]

n=len(larr)
length=8

print(rodCutProfit(larr,price,n,length))