maxn= 100009
level=[]
adj= []
dp= []
medge=[]
def ini():
    global maxn,dp,level,adj,medge
    level=[0]*maxn
    adj=[[] for i in range(maxn)]
    dp=[[-1 for j in range(20)]for i in range(maxn)]
    medge=[[0 for j in range(20)]for i in range(maxn)]
def dfs(u,p,w):
    global adj,dp,level,medge
    level[u]=level[p]+1
    dp[u][0]=p
    medge[u][0]=w
    for edge in adj[u]:
        if(edge[0]==p):
            continue
        dfs(edge[0],u,edge[1])
def pre(n):
    global dp,medge
    for j in range(1,20):
        for i in range(1,n+1):
            if(dp[i][j-1]!=-1):
                dp[i][j] = dp[dp[i][j - 1]][j - 1]
                medge[i][j] = max(medge[i][j - 1], medge[dp[i][j - 1]][j - 1])
def lca(u,v):
    global level,dp
    if(level[u]<level[v]):
        t=u
        u=v
        v=t
    diff=level[u]-level[v]
    for i in range(20):
        if(diff & (1<<i)):
            u=dp[u][i]
    if(u==v):
        return u
    for i in range(19,-1,-1):
        if(dp[u][i]!=dp[v][i]):
            u=dp[u][i]
            v=dp[v][i]
    return dp[u][0]

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        global maxn,adj,level,dp,medge
        ini()
        n=len(A) + 1
        for edge in A:
            adj[edge[0]].append((edge[1],edge[2]))
            adj[edge[1]].append((edge[0],edge[2]))
        dfs(1,0,0)
        pre(n)
        ans=[]
        for query in B:
            u=query[0]
            v=query[1]
            lc=lca(u,v)
            maxEdge=0
            diff1=level[u]-level[lc]
            diff2=level[v]-level[lc]
            for i in range(20):
                if(diff1 & (1<<i)):
                    maxEdge=max(maxEdge,medge[u][i])
                    u=dp[u][i]
                if(diff2 & (1<<i)):
                    maxEdge=max(maxEdge,medge[v][i])
                    v=dp[v][i]
            ans.append(maxEdge)
        return ans