def solve(arr1,arr2):
    dic ={}
    c =0
    for x in arr1:
        if x not in dic:
            dic[x] =1
            c+=1
    for num in arr2:
        if num not in dic:
            dic[num]=1
            c+=1
    return c


def solve2(arr1,arr2):
    s =set()
    for x in arr1:
        s.add(x)
    for y in arr2:
        s.add(y)
    return len(s)


arr1 = [18,20,18,15,20,5]
arr2 = [18,20,18,15,20,5,2,1,4]
re =solve(arr1,arr2)
res = solve2(arr1,arr2)
print(re)
print("Method2....................")

print(res)