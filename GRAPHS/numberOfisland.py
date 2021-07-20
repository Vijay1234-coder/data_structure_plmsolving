


'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 '''
class Solution:
    def numIslands(self, grid):
        count = 0

        visited = [[0 for i in range(501)] for j in range(501)]
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if (int(grid[i][j]) == 1 and visited[i][j] == 0):
                    self.dfs(i, j, n, m, grid, visited)
                    count += 1

        return count

    def dfs(self, i, j, n, m, grid, visited):

        if i < 0 or j < 0 or i >= n or j >= m:
            return

        if int(grid[i][j]) == 0 or visited[i][j] == 1:
            return

        if visited[i][j] == 0:
            visited[i][j] = 1
            self.dfs(i - 1, j, n, m, grid, visited)
            # self.dfs(i-1,j-1,n,m,grid,visited)
            # self.dfs(i-1,j+1,n,m,grid,visited)
            self.dfs(i, j - 1, n, m, grid, visited)
            self.dfs(i, j + 1, n, m, grid, visited)
            # self.dfs(i+1,j-1,n,m,grid,visited)
            self.dfs(i + 1, j, n, m, grid, visited)
            # self.dfs(i+1,j+1,n,m,grid,visited)
grid =[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s =Solution()
print(s.numIslands(grid))