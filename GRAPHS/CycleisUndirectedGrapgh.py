
'''IMPORTANT'''
'''intution : we will apply dfs and we dont go to parent supose if neighbour is already visited then we will check that
 it should not the parent of parent then it is making a loop '''

class Solution:
    def isCycle(self,V,adj):
        visited =[False]*V
        for i  in range(V):
            if visited[i] ==  False:
                if self.dfs(i,-1,visited,adj)==True:
                    return True
        return False
    def dfs(self,u,par,visited,adj):
        visited[u]=True

        for v in adj[u]:
            if visited[v]==False:
                if self.dfs(v,u,visited,adj)==True:
                    return True
            else:
                # if it is already visited then check wheather it is parent of u or not if it is not then return True
                if v!=par:
                    return True
        return False





T =int(input())
for i in range(T):
    V,E =map(int,input().split())
    adj =[[] for i in range(V)]
    for _ in range(E):
        u,v = map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    obj =Solution()
    ans = obj.isCycle(V,adj)
    if ans==True:
        print("1")
    else:
        print("0")




