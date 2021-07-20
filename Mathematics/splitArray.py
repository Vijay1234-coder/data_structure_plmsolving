'''Given an array arr[] of size N, the task is to split the entire array into a minimum number of subarrays such that for each subarray, the GCD of the first and last element of the subarray is greater than 1.

Examples:

Input: arr[] = {2, 3, 4, 4, 4, 3}
Output: 2
Explanation:
Split the given array into [2, 3, 4, 4, 4] and [3].
The first subarray has gcd(2, 4) = 2 which is more than 1 and
The second subarray has gcd(3, 3) = 3 which is also more than 1.

Input: arr[] = {1, 2, 3}
Output: 0
Explanation:
There is no possible splitting of the given array into subarrays in which the GCD of first and last element of the subarray is more than 1.'''

'''
Fix a right pointer to the last element of the original array arr[], and find the leftmost element in the original array such that GCD(left, right) > 1. If such an element is not found, there is no valid answer.
If such an element is found, that means we have found a valid subarray. Then change the right pointer to (left – 1), and again start searching for a valid subarray.
Repeat the above step until right is more than 0 and keep on increasing the count of subarrays found till now.
Print the value of count after all the above step'''

from math import gcd

r = gcd(0,0)
print(r)


