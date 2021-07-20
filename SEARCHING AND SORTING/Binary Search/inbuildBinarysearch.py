import bisect
import sys
arr = [1,2,3,5,4,6,7]
index=[0,1,2,3,4,5]
arr1 = [-sys.maxsize,sys.maxsize,sys.maxsize]

print(bisect.bisect_left(arr,6))
print(bisect.bisect_right(arr1,arr[1]))