class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_lis = {}

        for node in self.nodes:
            self.adj_lis[node] = []
    def add_edge(self,u,v):
        self.adj_lis[u].append(v)
        self.adj_lis[v].append(u)
    def degree(self,node):
        deg = len(self.adj_lis[node])
        return deg
    def print_adj_lis(self):
        for node in self.nodes:
            print(node,"->",self.adj_lis[node])


nodes = ["A","B","C","D","E"]
all_edges = [("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")]
graph  = Graph(nodes)
for u,v in all_edges:
    graph.add_edge(u,v)
graph.print_adj_lis()
print("Degree of C  : ",graph.degree("C"))