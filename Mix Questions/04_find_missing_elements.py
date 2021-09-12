'''consider an array  of non negative integers. A second array  is formed by shuffing the elements of the first array and deleting
 random  element. Given these two arrays , find  which element is missing in second  array. '''
def finder(arr1,arr2):
    count={}
    for num in arr1:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    for num in arr2:
        if num in count:
            count[num]-=1
        else:
            count[num]=1
    for k in count:
        if count[k]!=0:
            print("{} is missing element".format(k))
finder([1,2,3,4,5,6,7],[2,1,3,4,6])