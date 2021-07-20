class Solution:
    def minStepToReachTarget(self, KnightPos, TargetPos, N):

        si = KnightPos[0]
        sj = KnightPos[1]

        di = TargetPos[0]
        dj = TargetPos[1]

        if si == di and sj == dj:
            return 0

        visited = [[0 for i in range(N)] for i in range(N)]
        queue = []

        queue.append((si - 1, sj - 1))
        while queue != []:
            i, j = queue[0]
            queue.pop(0)
            if i - 2 >= 0 and j - 1 >= 0 and i - 2 < N and j - 1 < N and visited[i - 2][j - 1] == 0:
                visited[i - 2][j - 1] = visited[i][j] + 1
                queue.append((i - 2, j - 1))

            if i - 2 >= 0 and j + 1 >= 0 and i - 2 < N and j + 1 < N and visited[i - 2][j + 1] == 0:
                visited[i - 2][j + 1] = visited[i][j] + 1
                queue.append((i - 2, j + 1))

            if i - 1 >= 0 and j + 2 >= 0 and i - 1 < N and j + 2 < N and visited[i - 1][j + 2] == 0:
                visited[i - 1][j + 2] = visited[i][j] + 1
                queue.append((i - 1, j + 1))

            if i + 1 >= 0 and j + 2 >= 0 and i + 1 < N and j + 2 < N and visited[i + 1][j + 2] == 0:
                visited[i + 1][j + 2] = visited[i][j] + 1
                queue.append((i + 1, j + 2))

            if i + 2 >= 0 and j + 1 >= 0 and i + 2 < N and j + 1 < N and visited[i + 2][j + 1] == 0:
                visited[i + 2][j + 1] = visited[i][j] + 1
                queue.append((i + 2, j + 1))

            if i + 2 >= 0 and j - 1 >= 0 and i + 2 < N and j - 1 < N and visited[i + 2][j - 1] == 0:
                visited[i + 2][j - 1] = visited[i][j] + 1
                queue.append((i + 2, j - 1))

            if i + 1 >= 0 and j - 2 >= 0 and i + 1 < N and j - 2 < N and visited[i + 1][j - 2] == 0:
                visited[i + 1][j - 2] = visited[i][j] + 1
                queue.append((i + 1, j - 2))

            if i - 1 >= 0 and j - 2 >= 0 and i - 1 < N and j - 2 < N and visited[i - 1][j - 2] == 0:
                visited[i - 1][j - 2] = visited[i][j] + 1
                queue.append((i - 1, j - 2))

            return visited[di - 1][dj - 1]


