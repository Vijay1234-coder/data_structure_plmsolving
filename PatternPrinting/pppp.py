# 0
# 2 3
# 1 1 2
# 5 7 11 13
# 3 5 8 13 21



def util(n):
    listt=[0]*1000
    listt[0]=0
    listt[1]=1
    for i in range(2,1000):
        listt[i] = listt[i-1]+listt[i-2]
    return listt







def primes(n):
    p = [True]*1000
    prime =[]
    for i in range(2,1000):
        if p[i]==True:
            for j in range(i*i,1000,i):
                p[j]=False
    for i in range(2,1000):
        if p[i]==True:
            prime.append(i)
    return prime

def pattern(n):

    lis =util(1000)
    pr=primes(1000)
    n =5
    m=0
    x=0



    for i in range(1,6):
        for j in range(i):
            if i%2!=0:
                print(lis[m],end=" ")
                m+=1
            else:
                print(pr[x],end=" ")
                x+=1


        print(" ")

pattern(5)
