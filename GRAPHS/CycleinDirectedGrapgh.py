



def DFS(u,helper,visited):
    visited[u]=True
    helper[u] = True
    for v in adj_lis[u]:
        if helper[v]==True:
            return True
        if visited[v]==False:
            ans = DFS(v,helper,visited)
            if ans == True:
                return True
    helper[u] =False
    return False








def isCyclic(adj_lis,helper,visited):
    for node in adj_lis:
        if visited[node]==False:
            ans = DFS(node,helper,visited)
            if ans==True:
                return True
    return False









adj_lis = {    0: [1, 2],
               1: [2],
               2: [0, 3],
               3: [3]
               }
helper = {}
visited ={}

for node in adj_lis:
    helper[node]= False
    visited[node]= False
print(isCyclic(adj_lis,helper,visited))

