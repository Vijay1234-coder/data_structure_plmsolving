from itertools import combinations
# A Python program to print all combinations
# of given length with unsorted input.  
from itertools import combinations
s=[]
# Get all combinations of [2, 1, 3]  
# and length 2
a=[1,2,3,4,5,6]
for i in range(len(a)+1):
    comb =list(combinations(a,i))
    s.extend(comb)
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):






# Print the obtained combinations  

