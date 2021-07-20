q = 2
queries = []
ans = []
idx = [0]*q
for i in range(q):
    l = list(map(int,input("enter querie").split()))
    l[0]-=1
    l[1]-=1
    queries.append(l)
    idx[i] = queries[i]


queries.sort(key = lambda x:x[1])
m = [2,3]
real_index =idx.index(m)
print(real_index)



print(queries)
print(idx)