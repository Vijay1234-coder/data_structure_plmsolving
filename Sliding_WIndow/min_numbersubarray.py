from collections import deque




def minNumber(arr,k):
    n=len(arr)
    ans = []
    l = deque([])
    j=0
    i=0
    while(j<n):
        #calculation Part
        while(len(l)>0 and l[len(l)-1]>arr[j]):
            l.pop()
        l.append(arr[j])

        if (j-i+1<k):
            j+=1
        elif(j-i+1==k):
            #we choose answer from the calculation part
            ans.append(l[0])
            #before sliding the window we have to remove ith element if it take part in calculation

            if arr[i]==l[0]:
                l.popleft()

            i+=1
            j+=1
    return ans



print(minNumber([1,3,-1,-3,5,3,6,7],3))
