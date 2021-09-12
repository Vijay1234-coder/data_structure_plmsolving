







def seive(num):
    prime = [True for i in range(num+1)]
    p =2
    ans =[]
    while p*p<=num:
        if prime[p]==True:
            for i in range(p*p,num+1,p):
                prime[i]=False
        p+=1

    for i in range(2,num+1):
        if prime[i]==True:
            ans.append(i)
    return ans









print(seive(1000))
