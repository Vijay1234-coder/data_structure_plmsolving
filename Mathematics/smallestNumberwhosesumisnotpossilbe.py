#https://practice.geeksforgeeks.org/problems/b6b608d4eb1c45f2b5cace77c4914f302ff0f80d/1/

# a[i}>=1
def solve(arr):
    arr.sort()
    ans =1
    for x in arr:
        if x>ans:
            return ans
        ans+=x
print([1,2,6,3,2])

