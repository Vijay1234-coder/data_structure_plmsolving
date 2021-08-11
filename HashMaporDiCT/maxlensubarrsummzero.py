'''plm: find length of maximum subarray having sum of elements is equal to zero'''
'''https://www.youtube.com/watch?v=_yGf2rxwZlA'''
'''concept behind this if any sum appears more than one it means after fir sum appera sum of all elements aftr that array equal to zero'''
'''index:-1   2,8,-3,-5,2,-4,6,1,2,1,-3,4  
   sum:0      2,10,7, 2,4, 0  '''


def maxLenSubArray(arr):
    Max=0
    sum1=0
    i=-1

    dict1={sum1:i}
    while(i<len(arr)-1):
        i+=1
        sum1+=arr[i]

        if sum1 not in dict1:
            dict1[sum1]=i
        else:
            length = i-dict1.get(sum1)
            if(length>Max):
                Max=length
            # Max=max(Max,length)
    return Max









print(maxLenSubArray([2,8,-3,-5,2,-4,6,1,2,1,-3,4]))