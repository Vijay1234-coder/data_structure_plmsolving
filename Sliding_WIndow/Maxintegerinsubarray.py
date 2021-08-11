from heapq import heappop,heappush


'''Given an array of size N and integer k. find the max for each and every contigous subarray
of size K and also its index of max number that parent array'''

def max_number(arr,k):
    ans=[]
    i=0
    j=0
    n=len(arr)

    l = []


    while(j<n):
        #Calculation Part
        heappush(l,-arr[j])



        if(j-i+1<k):
            j+=1
        elif(j-i+1==k):
            # ANSWER
            ans.append(-l[0])
            # Sliding the Window and removing the element of i th index if it take part in calculation
            if(arr[i]==-l[0]):
                l.pop(0)

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

