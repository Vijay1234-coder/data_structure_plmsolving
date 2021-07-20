class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[0 for j in range(6)] for i in range(6)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.dfs(i, j, visited, 0, board, m, n, word) == True:
                    return True
        return False

    def dfs(self, i, j, visited, idx, board, m, n, word):

        if idx == len(word) - 1:
            return True
        visited[i][j] = 1

        if i > 0 and board[i - 1][j] == word[idx + 1] and visited[i - 1][j] == 0 and self.dfs(i - 1, j, visited,
                                                                                              idx + 1, board, m, n,
                                                                                              word):
            return True
        if j > 0 and board[i][j - 1] == word[idx + 1] and visited[i][j - 1] == 0 and self.dfs(i, j - 1, visited,
                                                                                              idx + 1, board, m, n,
                                                                                              word):
            return True
        if j < n - 1 and board[i][j + 1] == word[idx + 1] and visited[i][j + 1] == 0 and self.dfs(i, j + 1, visited,
                                                                                                  idx + 1, board, m, n,
                                                                                                  word):
            return True
        if i < m - 1 and board[i + 1][j] == word[idx + 1] and visited[i + 1][j] == 0 and self.dfs(i + 1, j, visited,
                                                                                                  idx + 1, board, m, n,
                                                                                                  word):
            return True

        visited[i][j] = 0

        return False






grid =[['A','B','C','E'],['S','F','C','S'],['S','D','E','E']]
n=3
m = 4
word ='ABCCED'
s =Solution()
print(s.find(grid,n,m,word))