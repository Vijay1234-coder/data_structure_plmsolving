
'''IPOR'''
'''Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
INPUT:[1]
output=[[1]]'''



def permutation(arr):
    result =[]

    if len(arr)==1:
        return [arr[:]]

    for i in range(len(arr)):
        n = arr.pop(0)
        perms =permutation(arr)


        for perm in perms:
            perm.append(n)

        result.extend(perms)

        arr.append(n)

    return result










arr = [1,2,3]
print(permutation(arr))