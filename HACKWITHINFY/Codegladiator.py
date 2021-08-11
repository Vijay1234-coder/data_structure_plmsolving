from math import sqrt
n = int(input())
arr = list(map(int, input().split()))

c =0

for i in range(n):
    flag =0
    v=[]
    if arr[i]!=1:
        while(arr[i]%2==0):
            v.append(2)
            arr[i]=arr[i]//2

        root =int(sqrt(arr[i]))
        for j in range(3,root+1,2):

            while(arr[i] % j==0):
                v.append(j)
                arr[i]=arr[i]//j
        if(arr[i]!=1):
            v.append(arr[i])
        v.reverse()
        x=1
        for j in range(len(v)):
            x=x*v[j]
            c=c+x
    c+=1
print(c)