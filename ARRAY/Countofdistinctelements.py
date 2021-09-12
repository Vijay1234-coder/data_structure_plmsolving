def solve(arr1,arr2):
    count =0
    dic = {}
    for x in arr1:
        if x not in dic:
            dic[x] =1
    for num in arr2:
        if num in dic:
            dic[num]-=1
            if dic[num]==0:
                count+=1
    return count




arr1 = [10,20]
arr2 =[20,30]


res = solve(arr1,arr2)
print(res)