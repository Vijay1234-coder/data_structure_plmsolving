''' Problem Statement-:  You have M questions and N seconds to complete a test.
    Each question has some points and takes some time to solve (which will be given as input).
    Find the maximum mark that can be scored by the student within the given time N.

Sample test case:

4 // number of questions
10 // Total time to attend the test
1 2 // one mark question – 2 seconds to solve.
2 3 // two mark question – 3 seconds to solve.
3 5 // three mark question – 5 seconds to solve.
4 7 // 4 mark question – 7 seconds to solve.
'''
t=[[-1 for j in range(1001)] for i in range(1001)]
def maxMarks(val,wt,n,w):
    if n==0 or w==0:
        return 0
    if t[n][w]!=-1:
        return t[n][w]
    if wt[n-1]<=w:
        t[n][w]= max(val[n-1]+maxMarks(val,wt,n-1,w-wt[n-1]), maxMarks(val,wt,n-1,w))
        return t[n][w]
    else:
        t[n][w]= maxMarks(val,wt,n-1,w)
        return t[n][w]




val=[1,2,3,4]
wt= [2,3,5,7]
w=10
n=len(wt)

print(maxMarks(val,wt,n,w))

