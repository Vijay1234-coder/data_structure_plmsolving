'''in this what we have calculated is largest sum possible'''
'''this algorithm has complexity O(N)'''

def largest_cont_sum(arr):
    max_sum=current_sum=arr[0]
    for num in arr[1:]:
        current_sum=max(current_sum+num,num)
        max_sum=max(current_sum,max_sum)
    return max_sum

largest_cont_sum([1,2,-1,3,4,10,10,-10,-1])
print(largest_cont_sum([1,2,-1,3,4,10,10,-10,-1]))

