#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def binarySearch(a, key):
    low = 0
    hig = len(a) - 1
    while (low <= hig):
        mid = low + (hig - low) // 2
        if (a[mid] == key):
            return mid
        elif a[mid] < key and key < a[mid - 1]:
            return mid
        elif a[mid] > key and key > a[mid + 1]:
            return mid + 1
        elif a[mid] < key:
            hig = mid - 1
        elif a[mid] > key:
            low = mid + 1
        else:
            return False


def climbingLeaderboard(ranked, player):
    n = len(ranked)
    m = len(player)
    res = [0] * m
    rank = [0] * n
    rank[0] = 1

    for i in range(1, n):
        if ranked[i] == ranked[i - 1]:
            rank[i] = rank[i - 1]
        else:
            rank[i] = rank[i - 1] + 1
    for i in range(0, m):
        playerscore = player[i]
        if playerscore > ranked[0]:
            res[i] = 1
        elif playerscore < ranked[n - 1]:
            res[i] = rank[n - 1] + 1
        else:
            index = binarySearch(ranked, playerscore)
            res[i] = rank[index]
    result = res
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
