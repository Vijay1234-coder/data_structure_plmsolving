import sys

# BUT This is O(N^2) solution
def solve(arr,k):
    Max =-sys.maxsize
    n =len(arr)
    for i in range(n):
        sum1 =0
        for j in range(i,n):
            sum1+=arr[j]
            if sum1 == k:
                Max =max(Max,j-i+1)
    return Max

print("EFFICIENT SOLUTION")
def solve_eff(arr,k):
    n =len(arr)
    mp = {}
    sum =0
    maxlen =0
    for i in range(n):
        sum +=arr[i]
        if sum ==k:
            maxlen =i+1
        elif sum-k in mp:
            maxlen =max(maxlen,i-mp[sum-k])
        if sum not in mp:
            mp[sum]=i   # here we are storing index till that sum
    return maxlen


arr = [-5, 8, -14, 2, 4, 12]
k = -5
print(solve(arr,k))
print(solve_eff(arr,k))