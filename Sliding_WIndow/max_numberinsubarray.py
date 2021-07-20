'''Given an array of size N and integer k. find the max for each and every contigous subarray
of size K and also its index of max number that parent array'''
from collections import deque
def max_number(arr,k):
    ans=[]
    i=0
    j=0
    n=len(arr)
    l=deque([])


    while(j<n):
        #Calculation Part
        while(len(l) > 0 and l[len(l)-1] < arr[j]):
            l.pop()
        l.append(arr[j])

        if(j-i+1<k):
            j+=1
        elif(j-i+1==k):
            # ANSWER
            ans.append(l[0])
            # Sliding the Window and removing the element of i th index if it take part in calculation
            if(arr[i]==l[0]):
                l.popleft()

            i+=1
            j+=1

    return ans




n=int(input("enter no elements in Array"))
arr=[]
for i in range(n):
    elements=int(input("enter elements"))
    arr.append(elements)
k=int(input("enter length of subarray"))
print(arr)
print(max_number(arr,k))

