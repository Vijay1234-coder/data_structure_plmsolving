

def subsets(m,index,n):

    if index==len(m):
        if len(n)!=0:
            print(n)

    else:
        subsets(m,index+1,n)
        subsets(m,index+1,n+m[index])
    return

a="abc"
n=""
subsets(a,0,n)
