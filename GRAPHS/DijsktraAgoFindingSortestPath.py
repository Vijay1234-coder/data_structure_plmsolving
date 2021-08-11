
''''IMPORTANT'''
'''DIJSktra ALgo'''

import sys
from queue import Queue
adj_lis = {
           1: {2: 2,3:4},
           2: {3: 1,4:7},
           3: {5: 3},
           4: {6: 1},
           5: {4:2, 6: 5},
           6:{}
           }

distance = {}
queue = Queue()
s = 1
distance[s]=0
for vertex in adj_lis:
    if vertex != s:
        distance[vertex]= sys.maxsize # or we can use infinity
queue.put(s)
while not queue.empty():
    u =queue.get()
    for v in adj_lis[u]:
        len_u_to_v = adj_lis[u][v]
        alt = distance[u]+len_u_to_v
        if alt < distance[v]:
            distance[v]=alt
        queue.put(v)
print(distance)








