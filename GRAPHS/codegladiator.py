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
    wprev =0
    while heap!=[]:
        currcost,u = heapq.heappop(heap)


        if parent[u] != None:
            wprev = graph[parent[u]][u]

        for v in graph[u]:
            w =graph[u][v]
            weight =w-wprev
            if weight<0:
                weight=0

            if visited[v]== False and distance[u] +weight < distance[v]:
                distance[v] = distance[u] + weight

                heapq.heappush(heap,(distance[v],v))
                parent[v] = u





        visited[u]=True
    if parent[dest]==None:
        return "NOT POSSIBLE"
    res = str(distance[dest])
    return res





n,e = map(int,input().split())
graph = defaultdict(dict)


for i in range(e):
    u, v, w = map(int, input().split())



    if v not in graph[u]:
        graph[u][v] =w


src =1
dest = n
print(graph)
print(shortestpath(graph,n,src,dest))
