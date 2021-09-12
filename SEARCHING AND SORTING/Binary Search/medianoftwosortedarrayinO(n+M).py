def median(a1,a2):
    n1 = len(a1)
    n2= len(a2)
    ans = [0]*(n1+n2)
    i=0
    j=0
    k=0
    while i<n1 and j<n2:
        if a1[i]<=a2[j]:
            ans[k] = a1[i]
            i+=1
            k+=1
        else:
            ans[k]=a2[j]
            j+=1
            k+=1
    while i<n1:
        ans[k] = a1[i]
        i+=1
        k+=1
    while j<n2:
        ans[k] =a2[j]
        j+=1
        k+=1

    print(ans)
    mid = (0 + (len(ans) - 1)) // 2
    if len(ans)%2==0:

        res = (ans[mid] + ans[mid+1])/2
    else:
        res = ans(mid)/1
    
    print(res)
    return






a1 =[10,20,30,40,50]
a2 = [5,15,25,35,45,55,65,75,85]
median(a1,a2)