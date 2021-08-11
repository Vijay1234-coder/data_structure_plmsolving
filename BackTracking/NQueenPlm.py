''' https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/'''
'''We have discussed Knight’s tour and Rat in a Maze problems in Set 1 and Set 2 respectively. Let us discuss N Queen as another example problem that can be solved using Backtracking.

The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. For example, following is a solution for 4 Queen problem.



The expected output is a binary matrix which has 1s for the blocks where queens are placed. For example, following is the output matrix for above 4 queen solution.

              { 0,  1,  0,  0}
              { 0,  0,  0,  1}
              { 1,  0,  0,  0}
              { 0,  0,  1,  0}'''

N = int(input("enter value of N"))
board = [[0 for i in range(N)]for j in range(N)]
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end =" " )
        print(" ")
def is_safe(row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i ,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i ,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True



def solverec(col):
    if col == N:
        return True
    for i in range(0,N):
        if is_safe(i,col)==True:
            board[i][col]=1
            if solverec(col+1)==True:
                return True
            board[i][col]=0
    return False





def solve():
    if solverec(0)==False:
        return False
    else:
        printSolution(board)
        return True


print(solve())