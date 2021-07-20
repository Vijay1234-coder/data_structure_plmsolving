'''  if left array Sum is equal to Right array Sum then middle element which
    separate left and right array is said to be
    equilibrium index   '''

''' arr = [1,2,4,2,1]
   o/p = 2
   explaination: arr[0]+arr[1] == arr[3]+arr[4]
   index = 2 is ans'''

'''O(N**2) approach'''



# def equilibriumIndex1(arr,n):
#     left_sum = 0
#     right_sum = 0
#
#     for i in range(n):
#         left_sum = 0
#         right_sum = 0
#
#         for j in range(i): # left sub array sum ith element is excluded so it separate lesft arrray
#             left_sum+=arr[j]
#         for j in range(i+1,n):
#             right_sum += arr[j]
#
#         if left_sum == right_sum:
#             return i
#     return -1


# arr = [-7,1,5,2,-4,3,0]
# n = len(arr)
# print("Solution with O(N**2)")
# print(equilibriumIndex1(arr,n))

print("____________________________ O(N) APPROACH ______________________________________")


def equilibriumIndex1(arr, n):
    left_sum  = 0
    right_sum = 0
    prefixSum = [0]*n  # prefixsum = [1, 3, 7, 8, 10]    arr= [1,2,4,1,2]
    prefixSum[0] = arr[0]
    # Edge cases
    if n==1:
        return 0
    if n==2:
        return -1
    for i in range(1,n):
        prefixSum[i] = prefixSum[i-1]+arr[i]

    total_sum  = prefixSum[n-1]   # total  sum of array

    for i in range(1,n-1):
        left_sum = prefixSum[i] -arr[i]
        right_sum = total_sum - prefixSum[i]

        if left_sum == right_sum:
            return i
    return -1

arr = [1,2,4,1,2]

n = len(arr)
print(equilibriumIndex1(arr,n))




