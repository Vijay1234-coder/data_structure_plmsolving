import sys
from collections import defaultdict
import heapq
def shortestpath(graph,n,src,dest):
    if e<n-1:
        return "NOT POSSIBLE"
    heap =[]
    distance ={}
    parent = {}
    visited = {}
    for v in range(1,n+1):
        distance[v] = sys.maxsize
        parent[v] =None
        visited[v] =False
    distance[src] = 0

    heapq.heappush(heap,(0,src))
    visited[src] = True
    c = 0

    while heap!=[]:
        currcost,u = heapq.heappop(heap)
        for v,w in graph[u]:
            if visited[v]== False and currcost+w < distance[v]:
                distance[v] = currcost + w
                heapq.heappush(heap,(distance[v],v))
                parent[v] =u

        visited[u]=True
    if parent[dest]==None:
        return "NOT POSSIBLE"
    res = str(distance[dest] - distance[parent[dest]])
    return res
dict ={}
parentt ={}
n,e = map(int,input().split())
graph = defaultdict(list)
for i in range(e):
    u,v,w = map(int,input().split())
    parentt[v] = [u,w]

for i in range(e):
    u, v, w = map(int, input().split())
    weight = w - parentt[v]

    graph[u].append((v,w))
print(parentt)

print(dict)

src =1
dest = n
print(shortestpath(graph,n,src,dest))
