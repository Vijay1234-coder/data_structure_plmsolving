class Graph:
    def __init__(self,nodes,is_directed=False):
        self.nodes = nodes
        self.adj_lis = {}
        self.is_directed = is_directed

        for node in nodes:
            self.adj_lis[node]=[]
    def edge(self,u,v):
        self.adj_lis[u].append(v)
        if self.is_directed==False:
             self.adj_lis[v].append(u)
    def DFSutil(self,s,visited):
        visited.add(s) # im adding source node to visited set
        print(s,end =" ")
        for adj_node in self.adj_lis[s]:
            if adj_node not in visited:
                self.DFSutil(adj_node,visited)



    def DFS(self):
        visited  =   set()
        for s in self.adj_lis:
            if s not in visited:
                 self.DFSutil(s,visited)

    def print_adj_lis(self):

            print(self.adj_lis)
nodes = [0,1,2,3]
edges =[(0, 1),
(0, 2),
(1, 2),
(2, 0),
(2, 3),
(3, 3)]

g=Graph(nodes,True)
for u,v in edges:
    g.edge(u,v)
g.print_adj_lis()
g.DFS()

