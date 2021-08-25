#https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1#

#Brute force

# arr =[8,5,6,0,0,2]
# n =len(arr)
#
# for i in range(n):
#     if arr[i]==0:
#         for j in range(i+1,n):
#             if arr[j]!=0:
#                 arr[i],arr[j]=arr[j],arr[i]
#
# print(arr)
#
arr =[8,5,6,0,0,2]
n =len(arr)
count =0
for i in range(n):
    if arr[i]!=0:
        arr[i],arr[count]=arr[count],arr[i]
        count+= 1
print(arr)

