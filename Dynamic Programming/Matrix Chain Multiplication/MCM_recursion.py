'''MCM QUESTION: '''


''' Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
The efficient way is the one that involves the least number of multiplications.
The dimensions of the matrices are given in an array arr[] of size N (such that N = number of matrices + 1)
where the ith matrix has the dimensions (arr[i-1] x arr[i]).

Example 1:

Input: N = 5
arr = {40, 20, 30, 10, 30}
Output: 26000
Explaination: There are 4 matrices of dimension 
40x20, 20x30, 30x10, 10x30. Say the matrices are 
named as A, B, C, D. Out of all possible combinations,
the most efficient way is (A*(B*C))*D. 
The number of operations are -
20*30*10 + 40*20*10 + 40*10*30 = 26000.  '''
import sys
def mcm(arr, i, j):
    Min = sys.maxsize

    if i >= j:
        return 0
    for k in range(i, j): # here k will go from i to j-1 because if k== j then k+1 will be return error out of bound see notes
        temp = mcm(arr, i, k)+mcm(arr, k+1, j)+arr[i-1]*arr[k]*arr[j]
        if temp<Min:
            Min  = temp
    return Min








arr = [40, 20, 30, 10, 30]
n = len(arr)
print(mcm(arr,1,n-1))
