def subSets(arr,index,sub):
    if index==len(arr):
        if len(sub)!=0:
            print(sub)
    else:
        subSets(arr,index+1,sub)
        subSets(arr,index+1,sub+[arr[index]])
    return sub





arr = [1,2,3]
n = len(arr)
subSets(arr,0,[])