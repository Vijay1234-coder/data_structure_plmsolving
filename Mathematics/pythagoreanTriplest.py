#Count number of triplets (a, b, c) such that a^2 + b^2 = c^2 and 1 <= a <= b <= c <= n


import math

n = int(input())
count =0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        x = i*i+j*j
        y = int(math.sqrt(x))

        if (y*y==x and y<=n):

            count+=1
print(count)


