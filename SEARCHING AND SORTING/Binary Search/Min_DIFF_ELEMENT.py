'''nice QUESTIOn'''
''' Given a sorted array, find the element in the array which has minimum difference with the given number  '''
'''arr = [1,2,3,4,8,10,13]
 x = 12   
o/p: 13 
explain: abs(13-12)=1 which is minimum  
 best case will be if target itself present in the array so min diff is 0 
  if target itself not present then we need to find number near to target '''


def binarySearch(arr,x):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = start+(end-start)//2
        if arr[mid]==x:
            return arr[mid]
        elif(x>arr[mid]):
            start =mid+1
        else:
            end= mid-1

    dif1 = abs(arr[end]-x)
    dif2 = abs(arr[start]-x)
    Min = min(dif1,dif2)
    if dif1 == Min:
        return arr[end]
    else:
        return arr[start]






arr = [1,2,3,4,8,10,13]
x = 12


print(binarySearch(arr,x))