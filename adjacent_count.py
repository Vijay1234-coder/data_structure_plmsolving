def adjacent_counter(arr):
    l=len(arr)
    cout1=0
    i=0
    j=0
    k=2
    while(j<l):
        if(j-i+1<k):
            j+=1
        elif(j-i+1==k):
            if(arr[j-1]==arr[j]):
                cout1+=1
            i+=1
            j+=1
    return cout1


print(adjacent_counter([1,2,2,3,4,4,4,4,10]))