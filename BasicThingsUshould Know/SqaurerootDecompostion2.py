import sys
from math import sqrt

block = [0]*100
block2 = [1000000]*100
arr =[0] *10000
blk_size =0


def query(l,r):
    Sum = 0
    Min =sys.maxsize
    while (l < r and l != 0  and l % blk_size != 0 ): # if l  lie in first block means block number 0 l%blk_size ==0 means l is starting of that block
        Sum += arr[l]
        Min = min(Min,arr[l])
        l += 1
    while (l + blk_size <= r):
        Sum += block[l//blk_size] #l//blok_size give block index in which l lie
        Min =min(Min,block2[l//blk_size])
        l += blk_size

    while(l<=r): # when l and r in same block then keep going till r
        Sum += arr[l]
        Min = min(Min,arr[l])
        l += 1

    return Sum,Min



def preprocess(input,n):
    global blk_size
    blk_size = int(sqrt(n))
    blk_idx = -1

    for i in range(n):
        arr[i] = input[i]
        if i % blk_size == 0:
            blk_idx += 1
        block[blk_idx] += arr[i]
        block2[blk_idx] =min(block2[blk_idx],arr[i])



input = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
n = len(input)
preprocess(input,n)
print(query(3,8))










