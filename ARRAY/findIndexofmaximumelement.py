import sys

Max = -sys.maxsize
arr = [2,3,1,5,6]
index =-1
for i in range(len(arr)):
    if arr[i] >Max:
        Max = arr[i]
        index = i
print(index)





