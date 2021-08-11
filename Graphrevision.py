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

g= Gra





nodes=[0,1,2,3,4]
g = Graph(nodes,True)
edges=[(0,4),(4,3),(3,2),(2,4),(2,1),(1,2),(1,0),(3,1)]
for u,v in edges:
    g.edge(u,v)

g.print_adj()

