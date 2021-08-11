def solve(arr,w):
    cur = w
    res =0
    for i in range(len(arr)):
        if arr[i][1]<=cur:
            cur-=arr[i][1]
            res+=arr[i][0]

        else:
            res += arr[i][0]* cur/arr[i][1]
            break
    return res









w = 50
arr = [(120,30),(100,20),(60,10)]
arr.sort(key = lambda x:x[0]/x[1],reverse=True)
result = solve(arr,w)
print(result)