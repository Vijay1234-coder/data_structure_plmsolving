'''Given an array A[] and a number x, check for pair in A[] with sum as x
Difficulty Level : Easy
Last Updated : 06 May, 2021'''
''' Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x. 

Examples: 

Input: arr[] = {0, -1, 2, -3, 1}
        sum =-2
Output: -3, 1
If we calculate the sum of the output,
1 + (-3) = -2

Input: arr[] = {1, -2, 1, 0, 5}
       sum = 0
Output: -1
No valid pair exists. '''
 # Complexity O(N)

def func(arr,x):
   dict1={}
   for i in range(len(arr)):
       compliment = x-arr[i]
       if compliment in dict1:
           return arr[i],compliment
       else:
           dict1[arr[i]]=1
   return -1






arr = [0, -1, 2, -3, 1]
x = -2
print(func(arr,x))