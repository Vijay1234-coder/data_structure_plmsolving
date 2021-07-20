# def seq_search(arr,key):
'''here array need not to be sorted'''
#     pos=0
#     found = False
#     while pos<len(arr) and found==False:
#         if arr[pos]==key:
#             found=True
#         else:
#             pos+=1
#     return found
#
#
# arr=[1,2,3,4,5,6]
# print(seq_search(arr,6))








def ordered_seq_search(arr,target):
    '''arr should be sorted then we know if element at certain position is greater than key we have to stop there '''
    pos=0
    found = False
    stopped =  False
    while pos<len(arr) and (found==False) and (stopped == False):
        if arr[pos]==target:
            found=True
        else:
            if arr[pos] > target:
                stopped = True
            else:
                pos+=1

    return found


arr=[1,2,3,4,5,6]
print(ordered_seq_search(arr,6))