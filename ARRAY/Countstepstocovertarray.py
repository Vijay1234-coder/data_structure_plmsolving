'''Important'''
'''Count minimum steps to get the given desired array
Consider an array with n elements and value of all the elements is zero. We can perform following operations on the array. 
 

Incremental operations:Choose 1 element from the array and increment its value by 1.
Doubling operation: Double the values of all the elements of array.
Input: target[] = {2, 3} 
Output: 4
To get the target array from {0, 0}, we 
first increment both elements by 1 (2 
operations), then double the array (1 
operation). Finally increment second
element (1 more operation)

Input: target[] = {2, 1} 
Output: 3
One of the optimal solution is to apply the 
incremental operation 2 times to first and 
once on second element.

Input: target[] = {16, 15, 16}     
Output: 7
The output solution looks as follows. First 
apply an incremental operation to each element. 
Then apply the doubling operation four times. 
Total number of operations is 3+4 = 7   '''
'''aproach:
 Take the target array first. 

Initialize result as 0. 

If all are even, divide all elements by 2 
and increment result by 1. 

Find all odd elements, make them even by 
reducing them by 1. and for every reduction,
increment result by 1.

Finally, we get all zeros in target array'''



def countsteps(target):
    n   = len(target)
    res = 0

    while True:
        zero_count = 0

        i =0
        while(i<n):

            #to check if atleast one element is not even then break
            if target[i] % 2!=0:
                break
            elif (target[i]==0):
                zero_count+=1
            i+=1

        if zero_count == n:
            return res
        if i == n: # all even element in array
            for j in range(n):
                target[j] = target[j]//2
            res+=1
        for j in range(i,n):  #4 3 4
            if target[j]%2!=0:
                target[j]= target[j]-1
                res+=1














arr = [16,16,16]
print(countsteps(arr))