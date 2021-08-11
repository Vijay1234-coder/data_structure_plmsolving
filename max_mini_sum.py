import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum1 = 0
    sum2 = 0
    arr.sort()
    print(arr)
    for i in range(0,n-1):
        sum1 += arr[i]
    for i in range(0, n-1):
        sum2 += arr[i+1]
    print(sum1,sum2)


if __name__ == '__main__':
    arr = list(map(int, input("enter array").rstrip().split()))
    n = len(arr)

    miniMaxSum(arr)
