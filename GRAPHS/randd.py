# graph ={
#
#     1:{ },
#     2:{}
# }
# nodes = [(2,30),(3,3000)]
# for i in range(len(nodes)):
#     if nodes[i][0] not in graph[1]:
#         graph[1][nodes[i][0]] =nodes[i][1]
#     else:
#         continue
# print(graph)

N=5
R=5
graph1 ={}
for i in range(1,N+1):
    graph1[i]={}
for i in range(R):
    x= list(map(int,input().split()))
    u = x[0]
    v =x[1]
    w = x[2]
    if v not in graph1[u]:
        graph1[u][v] =w
    else:
        continue
print(graph1)

