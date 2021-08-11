
'''IMPORATNT'''
'''Time Complexity in Building a MAx Heap will be O(Logn) becuze we swaping till height of tree which is log(n)'''
def max_heapify(A,n,i):
    left = 2*i+1  # index of its left child
    right = 2*i +2  # index of its right child

    if left <= n and A[left]>A[i]:
        largest = left
    else:
        largest = i
    if right <= n and A[right] > A[largest]:
        largest = right

    if largest != i:
        #swap(A[i],A[largest])
        A[i],A[largest] =A[largest],A[i]
        max_heapify(A,n,largest)














def built_max_heap(A):
    n = len(A)
    # we start with none leaf nodes
    # no. of leaf nodes in complete binary tree
    # n/2+1 ceil val to n
    # so non leaf nodes node will be n//2

    for i in range(n//2-1,-1,-1): # we will start from last none leaf node which at n-1 index
        max_heapify(A,n,i)







A =[1,6,5,0,8,2,7]

built_max_heap(A)
print(A)