from math import sqrt
n = int(input())
arr = list(map(int, input().split()))
pm = [2,3,5,7,11,13,17,19,23,29]
c=0
for i in range(n):
    v =[]
    if arr[i]!=1:
        root = int(sqrt(arr[i]))
        flag = 0
        x =0
        for j in range(2,root+1):

            rem = arr[i]%j
            if rem ==0 and j in pm:
                flag = 1
                x = j
                break


        if flag==0:
            c = c+ arr[i]+1
        else:

            v.append(arr[i])
            while arr[i]>1:

                v.append(arr[i]//x)
                arr[i]= arr[i]//x
            c += sum(v)




    else:
        c += arr[i]
print(c)







