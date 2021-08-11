l =1
r =100
def primeinrange(l,r):
    prime=[True]*(r-l+1+1)
    if l<=1:
        prime[l]=False

    for i in range(2,r+1):
        if prime[i]==True:
            for j in range(i*i,101,i):
                prime[j]=False
    for x in range(2,len(prime)):
        if prime[x]==True:
            print(x,end=" ")
    # print(prime)
primeinrange(l,r)