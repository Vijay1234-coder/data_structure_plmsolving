''' IMPORTANT '''
'''   if there is n nodes given then minimum number of edges required to connect nodes is : n-1 '''
'''   if present edges is less than n-1 then its not possible to connect all nodes  '''

'''  in below question 
1. we checked how many extra nodes occupied by  input connected nodes 
2. we count   how many clusters of connected nodes
for example if group of connected  graph is C then C-1 will be minimum number of edges requred to connect all n nodes '''

class Solution:
    def makeConnected(self, n, connections):

        if len(connections) < n - 1:  # if number of edges is less than  total no. of required edges means n-1
            return -1
        graph = []
        for i in range(n):
            graph.append([])
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        vis = [0] * n
        c = 0
        for i in range(n):
            if vis[i] == 0:
                c += 1
                self.dfs(i, graph, vis)
        return c - 1

    def dfs(self, u, graph, vis):
        vis[u] = 1
        for v in graph[u]:
            if vis[v] == 0:
                self.dfs(v, graph, vis)


connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
n =6
s = Solution()
print(s.makeConnected(6,connections))

