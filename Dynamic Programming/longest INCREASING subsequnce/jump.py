# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
import sys
def solve(arr,N):
    jump =[sys.maxsize]*N

    if arr[0]==0:
        return False
    jump[0]=0
    for i in range(1,N):
        for j in range(0,i):
            if i <= j+arr[j]:
                jump[i] = min(jump[i],jump[j]+1)
    return jump[-1]










N = 11
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

print(solve(arr,N))