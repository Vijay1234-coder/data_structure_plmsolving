
n =int(input("enter value of N"))
t = [[0 for j in range(n+2)] for i in range(n+2)]
for i in range(1,n+1):
    for j in range(1,n+1):
        # t[i][j]=int(input("enter value of matrix"))
        t[i][j] = int(input(" enter eleme"))


i = int(input("enter Value of X"))
j =int(input("Enter value of Y"))
i = i+1
j = j+1
Ans = t[i-1][j-1]+t[i-1][j]+t[i-1][j+1] + t[i][j-1] + t[i][j+1] + t[i+1][j-1]+t[i+1][j]+t[i+1][j+1]
print(Ans)