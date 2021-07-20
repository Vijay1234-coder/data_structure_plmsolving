''''''
''' DFS always return Forest but BFS return TREE'''




adj_list = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["B","F"],
    "D":[],
    "E":["F"],
    "F":[],
}



color = {} # W ,G, B here white means its not visited at all grey means visited once black means completly visited
parent = {}
trav_time = {} #[start, end] means when visited at starting and when it completely  visited
dfs_traversal_output = []

#initialize

for node in adj_list.keys():
    color[node] ="W" # not visited
    parent[node] = None
    trav_time[node] = [-1,-1] # it means not traversed


time = 0
def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1


# dfs_util("A") # here we are providing source node
# print(dfs_traversal_output)
# print(parent)
# for node in adj_list:
#     print(node,"-->",trav_time[node])
# but what is grap is not connected
#then


# if don't want traverse with source node Below is valid for the unconnected graph also
for u in adj_list:
    if color[u]=="W":
        dfs_util(u)
print(dfs_traversal_output)
for node in adj_list:
    print(node,"-->",trav_time[node])




