'''Longest Common Substring(Dynamic Programming)
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
Examples:

Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
Output : 5
The longest common substring is “Geeks” and is of length 5.'''


def longCommSubstring(x,y,m,n):
    Max=0
    t=[[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(0,m+1):
        t[i][0] = 0
    for j in range(1,n+1):
        t[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(x[i-1]==y[j-1]):
                t[i][j] = t[i-1][j-1] + 1  # if consecutive char are matching then increase by one
            else:
                t[i][j] = 0   # if consecutive numbers are not same then count will zero
    for i in range(m+1):
        for j in range(n+1):
            Max=max(Max,t[i][j])

    return Max

x= "GeeksforGeeks"
y= "GeeksQuiz"
m=len(x)
n=len(y)
print(longCommSubstring(x,y,m,n))
