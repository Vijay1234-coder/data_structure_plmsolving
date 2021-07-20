adj_lis = {0: [1, 2],
           1: [2],
           2: [0, 3],
           3: [3]
           }
visited = {}
stack =   []
for node in adj_lis:
    visited[node]=False
s=2

stack.append(s)
cycle=[]
visited_count ={s:1}
dfsout = []
while stack!=[]:
    u =stack.pop()
    dfsout.append(u)
    visited[u] =True
    for v in adj_lis[u]:
        if visited[v]==False:
            stack.append(v)
        else:
            print(True)



print(dfsout)

