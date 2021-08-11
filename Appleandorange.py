#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_lis = []
    orange_lis = []

    count1 = 0
    count2 = 0

    for i in range(len(apples)):
        apples[i] += a
        apple_lis.append(apples[i])

    for i in range(len(oranges)):
        oranges[i] += b
        orange_lis.append(oranges[i])
    for num in apple_lis:
        if num in range(s, t + 1):
            count1 += 1
    print(count1)

    for num in orange_lis:
        if num in range(s, t + 1):
            count2 += 1
    print(count2)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
