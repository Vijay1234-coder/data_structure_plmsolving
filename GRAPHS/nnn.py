import time
start_time = time.time()
import sys
from queue import Queue
def main(adj_lis):
    if R<N-1:
        return "NOT POSSIBLE"

    distance ={}

    s = 1
    par ={}
    distance[s]=0
    for vertex in adj_lis:
        if vertex==1 and adj_lis[vertex]==[]:
            return "NOT POSSIBLE"

        par[vertex]= None
        if vertex != s:
            distance[vertex]  =  sys.maxsize # or we can use infinity
    queue = Queue()
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(len(adj_lis[u])):
            len_u_to_v = adj_lis[u][v][1]
            alt = distance[u]+len_u_to_v
            if alt < distance[adj_lis[u][v][0]]:
                distance[adj_lis[u][v][0]] = alt
                par[adj_lis[u][v][0]] = u
            queue.put(adj_lis[u][v][0])
    for x in par:
        if x!=1 and par[x]==None and x==N :
            return "NOT POSSIBLE"



    print("pare size",sys.getsizeof(par))
    res = (distance[N] - distance[par[N]])
    return res


inputt =list(map(int, input().split()))
N =inputt[0]
R =inputt[1]


adj_lis = {}
for i in range(1,N+1):
    adj_lis[i]=[]


for i in range(R):
    x = list(map(int, input().split()))
    u = x[0]
    v = x[1]
    w = x[2]
    adj_lis[u].append([v,w])




print(main(adj_lis))
print("--- %s seconds ---" % (time.time() - start_time))
