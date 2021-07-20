from collections import  defaultdict

x = 0

def dfs(u,d,graph,path,visited,ans):
    visited[u] = True
    path.append(u)


    if u==d:
        global x

        x+=1


        print(path)


    for v in graph[u]:
        if visited[v]==False:
            dfs(v,d,graph,path,visited,ans)
    path.pop()
    visited[u] = False

def allpath(graph,s,d,N):

    ans = []
    count =0
    visited = [False]*N
    path =[]
    dfs(s,d,graph,path,visited,ans)







N,E = map(int,input().split())
s,d = map(int,input().split())
graph = defaultdict(list)
for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)

print(allpath(graph,s,d,N))











