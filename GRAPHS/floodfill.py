'''IMPORTANT'''
'''An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from 
the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 
4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 
4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

 '''




class Solution:
    def floodFill(self, image ,sr, sc, newColor):
        m = len(image)
        n = len(image[0])

        old_color = image[sr][sc]
        visited = [[0 for i in range(51)] for j in range(51)]
        self.dfs(sr, sc, visited, old_color, newColor, image, m, n)
        return image

    def dfs(self, i, j, vis, old_color, newColor, image, m, n):
        if (i < 0 or j < 0 or i >= m or j >= n):
            return
        if vis[i][j] == 1:
            return
        if image[i][j] != old_color:
            return

        if image[i][j] == old_color:
            image[i][j] = newColor

        vis[i][j] = 1

        self.dfs(i - 1, j, vis, old_color, newColor, image, m, n)
        self.dfs(i, j - 1, vis, old_color, newColor, image, m, n)
        self.dfs(i, j + 1, vis, old_color, newColor, image, m, n)
        self.dfs(i + 1, j, vis, old_color, newColor, image, m, n)
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

s =Solution()
print(s.floodFill(image,sr,sc,newColor))