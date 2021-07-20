'''Strongly Connected Graph means every node connect whether directly or indectly'''

class Graph:
    def __init__(self,nodes,is_directed=False):
        self.nodes =nodes
        self.adj_lis ={}
        self.is_directed = is_directed


        for node in nodes:
            self.adj_lis[node]=[]


    def edge(self,u,v):
        self.adj_lis[u].append(v)
        if self.is_directed==False:
            self.adj_lis[v].append(u)

    def print_adj_lis(self):
        print(self.adj_lis)
    def DFSutil(self,u,visited):
        visited[u]=True
        for v in self.adj_lis[nodes[u]]:
            if visited[nodes.index(v)] == False:
                self.DFSutil(v,visited)

    def DFS(self):



       for i in range(n):
           visited=[False]*n

           if visited[i]==False:
               self.DFSutil(i,visited)
           for u in visited:
               if visited[u]==False:
                   return False
       return True





















n=5
nodes=[0,1,2,3,4]
edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]
g = Graph(nodes,True)

for u,v in edges:
    g.edge(u,v)

g.print_adj_lis()
print(g.DFS())
