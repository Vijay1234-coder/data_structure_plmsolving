'''IMPORTANT'''
''' Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR. '''
# CoMPLEXITY IS O((n^2))^4


class Solution:
    def findPath(self, m, n):
        global ans    # because we will use in another method
        ans = []
        visited = [[0 for i in range(n)] for j in range(n)] # visited array will keep track
        if m[0][0] == 0 or m[n - 1][n - 1] == 0: # edge case if source or destination is zero then not possible
            return ans
        s = ""   # This will store the "U" "D" "L" "R"
        self.dfs(0, 0, s, m, n, visited) # we will visite all the possible neighbours so dfs starts from 0,o
        ans.sort() # This asked in question to sort the ans at the end
        return ans

    def dfs(self, i, j, s, m, n, visited):
        if i < 0 or j < 0 or j >= n or i >= n: # base case that we can't jump out of the matrix
            return
        if m[i][j] == 0 or visited[i][j] == 1: # if i,j position is zero or its is already visited we should return
            return
        if i == n - 1 and j == n - 1: # base case if i and j reached destination then what ever the string we have calculated store it in ans
            ans.append(s)

        visited[i][j] = 1 # after reaching there mark it visited
        self.dfs(i - 1, j, s + "U", m, n, visited)  # call dfs on all possible direction
        self.dfs(i + 1, j, s + "D", m, n, visited)
        self.dfs(i, j - 1, s + "L", m, n, visited)
        self.dfs(i, j + 1, s + "R", m, n, visited)

        visited[i][j] = 0  # if u reached zero position or already visited position then back track and mark it unvisited


s =Solution()
m=[      [1, 0, 0, 0],
         [1, 1, 0, 1],
         [1, 1, 0, 0],
         [0, 1, 1, 1]   ]
n = 4

print(s.findPath(m,n))