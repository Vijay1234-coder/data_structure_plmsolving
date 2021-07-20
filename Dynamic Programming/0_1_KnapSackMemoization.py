
'''hdhdd'''

''' Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
 In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
  Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this
  subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).'''
'''.......Below code is recursion complexity is more need to memoizize so that solution converted into dp'''
# def knapSack(wt,val,w,n):
#     #base condition
#     if(n == 0 or w == 0) :
#         return 0
#
#     # choice diagram
#     if(wt[n-1]<=w):
#         return max(val[n-1]+knapSack(wt,val,w-wt[n-1],n-1),knapSack(wt,val,w,n-1))
#     elif(wt[n-1]>w):
#         return knapSack(wt,val,w,n-1)
#
#
#
#
#...................Recursion + Memoization =DP....................more efficient.........................

#constarints n=100 and W=1000


t= [[-1 for j in range(1002)] for i in range(102)]        # t[n+1][w+1]

def knapSack(wt,val,w,n):
    #base condition
    if(n == 0 or w == 0) :
        return 0
    if t[n][w]!=-1:
        return t[n][w]


    if(wt[n-1] <= w ):
        t[n][w] = max(val[n-1]+knapSack(wt,val,w-wt[n-1],n-1),knapSack(wt,val,w,n-1))
        return t[n][w]
    elif(wt[n-1]>w):
        t[n][w] = knapSack(wt,val,w,n-1)
        return t[n][w]



val = [60, 100, 120]
wt = [10, 20, 30]
w = 50
n = len(val)
print(knapSack(wt,val,w,n))























