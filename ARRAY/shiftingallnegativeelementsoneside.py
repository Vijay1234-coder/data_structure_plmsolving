arr1 =[-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr=[-1,-2,1,0,2]
op =[-12,-13,-5,-7,-3,-6, 11, 6, 5]

n =len(arr)
j =0
for i in range(n):
    if arr[i]<=0:
        arr[i],arr[j] = arr[j],arr[i]
        j+=1
print(arr)

for i in range(n):
    if arr[i]>0:
        print(arr[i:])
        break

# print(arr1)

