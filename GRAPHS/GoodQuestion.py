from queue import Queue



def solve(arr):
    x =1
    for i in range(len(arr)):
        if arr[i]==x:

            x+=1
            arr[i]=x
        elif arr[i]>x:
            arr[i]=x
    return arr[-1]

Result =[]
n = 4
val = [1,3,2,8]
parent = [1,2,2]
ans =[2,2,3,4,2,5]
graph ={}
for i in range(1,n+1):
    if i not in graph:
        graph[i]=[]
for i in range(1,n):
    graph[parent[i-1]].append(i+1)
parent ={}
visited ={}
for node in graph:
    visited[node]=False
    parent[node]= None
print(graph)

queue =Queue()
s = 1
visited[s]=True
queue.put(s)
while not queue.empty():
    u = queue.get()
    for v in graph[u]:
        if visited[v]==False:
            visited[v]=True
            parent[v]= u
            queue.put(v)


print(parent)

for i in range(1,n+1):
    v =i

    path = []
    while v is not None:  # we will go till our source  node ' parents become false the loop at source node
        path.append(val[v - 1])
        v = parent[v]
    path.reverse()
    path.sort()

    res = solve(path)
    Result.append(res)


print(Result)




