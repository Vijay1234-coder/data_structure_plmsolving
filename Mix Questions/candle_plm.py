#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    count1 = {}
    count2 = 0
    candles.sort()
    for num in candles:
        if num in count1:
            count1[num] += 1
        else:
            count1[num] = 1

    k = list(count1.keys())[-1]
    print(count1[k])

    # Write your code here


if __name__ == '__main__':


    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))
    n = len(candles)

    result = birthdayCakeCandles(candles)




