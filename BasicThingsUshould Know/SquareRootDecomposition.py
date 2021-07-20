'''square root decomposition '''
'''
RMQSQ - Range Minimum Query

You are given a list of N numbers and Q queries. Each query is specified by two numbers i and j; the answer to each query 
is the minimum number between the range [i, j] (inclusive).

Note: the query ranges are specified using 0-based indexing.

Input
The first line contains N, the number of integers in our list (N <= 100,000). The next line holds N numbers that are
 guaranteed to fit inside an integer. Following the list is a number Q (Q <= 10,000). The next Q lines each contain two
  numbers i and j which specify a query you must answer (0 <= i, j <= N-1).

Output
For each query, output the answer to that query on its own line in the order the queries were made.

Example
Input:
3
1 4 1
2
1 1
1 2
Output:
4
1'''

from sys import maxsize
from math import sqrt
def getMin(l,r):
    n = len(arr)


    BLK = int(sqrt(n))   # we divide the whole array into block size of sqrt(n) and number of such block will be n//BLK
    LB = l // BLK   # BLK is block size
    RB = r//BLK
    Min = maxsize


    num_Of_Blks = n // BLK
#...................Below code for storing results in each block index ....................................
    EachBLK_result = [0]*num_Of_Blks

    for i in range(num_Of_Blks):
        Min1 = maxsize

        if  i == num_Of_Blks-1:
            for j in range(BLK*i,n):
                Min1 = min(Min1,arr[j])
                break

        for j in range(BLK*i,(i+1)*BLK):
            Min1 = min(Min1,arr[j])
        EachBLK_result[i] = Min1     # F arr








    if(LB==RB):
        for i in range(l,r+1):
            Min = min(Min,arr[i])
    else:
        # block no. x start from  index y then y = blk*x
        for i in range(l,(LB+1)*BLK):
            Min = min(Min,arr[i])
        for i in range(LB+1,RB):
            Min = min(Min,EachBLK_result[i]) # here F[i] already calculated result in given Block
        for i in range(RB*BLK,r+1):
            Min = min(Min,arr[i])
    return Min
















arr = [1,5,2,3,6,4,8,5,6,4,-2,6]
# possible_blocks = [1,5,2][3,6,4][8,5,6][4,1,6]
# each_BLK_result =[  1      3      5      2]
# index_block =       [0]    [1]    [2]   [3]
print(getMin(1,10))
q = [1,10]



