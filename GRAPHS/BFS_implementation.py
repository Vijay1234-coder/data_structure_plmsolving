from queue import Queue
adj_list  = {
    "A":["B","D"],
    "B":["A",'C'],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H",],
    "H":["F","G"]
}

visited = {}
level = {}  # distance dictionary
parent = {}

bfs_traversal_output = []
queue = Queue()

for node in adj_list.keys():
    visited[node]=False # initially all the Nodes are not visited
    parent[node] = None # initially parent of each Node is Null
    level[node] = -1    # initially we don't know about the level so initialize with -1

s = "A"                 # we marked it as source node
visited[s] = True
level[s] = 0
parent[s] = None # parent of source node is none
queue.put(s)  # Adding source node to queue
while not queue.empty(): # become false when queue empty and loop breakes
    u = queue.get()  # it will pop the first element of queue
    bfs_traversal_output.append(u) # we store the popped element from queue
    # now explore all the adjacent vertex of u
    for v in adj_list[u]:
        # we will check adjacent vertex is already visited or not if yes then will not visit
        if visited[v] == False: # IF Not visited  then visit it
            visited[v] = True # mark visited True now it is visited
            # now mark parent of that vertex v is u
            parent[v] = u
            level[v] = level[u]+1
            # now add that vertex v in queue
            queue.put(v)
print(bfs_traversal_output)
# Q: shortest Distance of "H" from source node is
print(f"Shortest Distance of H from Source Node is {level['H']} ")
# print Shortest Path Of G from source Node
v = "G"
path =[]
while v is not None:  # we will go till our source  node ' parents become false the loop at source node
    path.append(v)
    v = parent[v]
path.reverse()
print(path)












