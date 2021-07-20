

def xor(arr,n):
    result =0
    for i in range(n):
        result =result^arr[i]
    return result

arr= [3, 9, 12, 13, 15]
n =len(arr)
print(xor(arr,n))










