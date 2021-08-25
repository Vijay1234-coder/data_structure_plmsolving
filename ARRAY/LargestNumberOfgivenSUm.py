#https://practice.geeksforgeeks.org/problems/largest-number-with-given-sum-1587115620/1

class Solution:
    # Function to return the largest possible number of n digits
    # with sum equal to given sum.
    def largestNum(self, n, s):
        if s == 0:
            if n == 1:
                return 0
            else:
                return -1
        if s > 9 * n:
            return -1
        else:
            res = [0] * n

            for i in range(n):
                if s >= 9:
                    res[i] = 9
                    s -= 9
                else:
                    res[i] = s
                    s = 0
        x = 0
        for i in range(n):
            x = x * 10 + res[i]
        return x

