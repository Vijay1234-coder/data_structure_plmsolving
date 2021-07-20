
''''''
'''TWO POINTER :array  Must be SORTED and Finding sum of any two element is equal to given x if present return True '''
'''This Problem Based on two pointer algo'''
''' return True if sum of any triplet in an array is Zero'''

global  list_store_element
def twoPointer(arr,x,i):



    j= len(arr)-1
    while(i<j):
        if arr[i]+arr[j]== x:
            list_store_element[1] = arr[i]
            list_store_element[2] =arr[j]

            return True
        elif(arr[i]+arr[j]>x): # [-1,0,1,2,3,3,10 ]
            j-=1
        elif(arr[i]+arr[j]<x):
            i+=1
    return False


def findTriplet(arr,n):

    arr.sort()
    for i in range(n-2):
        if (twoPointer(arr,-arr[i],i+1)==True):
            list_store_element[0]=arr[i]
            print(list_store_element)

            return True
    return False





arr = [0, -1, 2, -3, 1]
n = len(arr)
list_store_element = [0]*3  # initialize array for storing such triplets
print(findTriplet(arr,n))



