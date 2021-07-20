def insert(a,temp):
    #[0,1,5]  ,     2
    if len(a)==0 or a[len(a)-1] <= temp:
        a.append(temp)
        return a

    else:
        val= a[len(a)-1]
        a.pop()
        #[0,1]  , temp=2 , val=5
        insert(a,temp)
        a.append(val)





def sortRecurr(a):  #1,0,5,2
    #base condition
    if len(a)==1:
        return a
    else:
        temp= a[len(a)-1]   # temp=2
        a.pop()         #1,0,5
        sortRecurr(a)
        insert(a,temp)  #[1,0,5] , 2
    return a











a=[1,0,5,2]

print(sortRecurr(a))