#https://www.geeksforgeeks.org/length-of-longest-subarray-with-equal-number-of-odd-and-even-elements/
import sys


def solve1(arr,n):
    Max =-sys.maxsize
    for i in range(n):
        odd_count =0
        even_count =0
        for j in range(i,n):
            if arr[j]%2==0:
                even_count+=1
            else:
                odd_count+=1
            if odd_count==even_count:
                Max = max(Max,odd_count*2)

    return Max


def solve2(arr,n):
    mp ={'odd':0,'even':0}
    Max = -sys.maxsize

    for i in range(n):
        if arr[i]%2==0:
            mp['odd']+=1
        else:
            mp['even']+=1
    for k in mp:
        Min =min(mp['odd'],mp['even'])
    return Min*2








arr = [12, 4, 7, 8, 9, 2, 11, 0, 2, 13]

n =len(arr)
res  = solve1(arr,n)
res2 =solve2(arr,n)
print(res2)