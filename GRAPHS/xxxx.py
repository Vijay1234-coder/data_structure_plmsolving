


import sys
from queue import Queue


def main(adj_lis):
    if R<N-1:
        return "NOT POSSIBLE"

    distance ={}

    s = 1

    distance[s]=0
    for vertex in adj_lis:
        if vertex==1 and adj_lis[vertex]==[]:
            return "NOT POSSIBLE"


        if vertex != s:
            distance[vertex]  =  sys.maxsize # or we can use infinity
    queue = Queue()
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in adj_lis[u]:
            len_u_to_v = adj_lis[u][v]
            alt = distance[u]+len_u_to_v
            if alt < distance[v]:
                distance[v] = alt

            queue.put(v)
            l = u



    if distance[N]==sys.maxsize:
        return "NOT POSSIBLE"





    print("distance size",sys.getsizeof(distance))
    res =distance[N]-distance[l]
    return res


inputt =list(map(int, input().split()))
N =inputt[0]
R =inputt[1]


adj_lis ={}
for i in range(1,N+1):
    adj_lis[i]={}
for i in range(R):
    x= list(map(int,input().split()))
    u = x[0]
    v =x[1]
    w = x[2]
    if v not in adj_lis[u]:
        adj_lis[u][v] =w
    else:
        continue



print(main(adj_lis))
print("size adj_lis",sys.getsizeof(adj_lis))











