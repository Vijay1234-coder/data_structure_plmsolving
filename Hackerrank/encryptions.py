
import math
from math import sqrt
s ="iffactsdontfittotheorychangethefacts"


col = int(math.ceil(sqrt(len(s))))
row = int(math.floor(sqrt(len(s))))
print(col)
print(row)

s1 = ""
for i in range(col):
    for j in range(i,len(s),row):
        s1 = s1+s[j]
    print(s1, end=" ")
    s1=""
