import sys
from itertools import combinations

def MaxVal(S,Q):

    Max =-20000000000000000000000
    res1 = [S[x:y] for x,y in combinations(range(len(S)+1),r=2)]
    res2 = [Q[x:y] for x,y in combinations(range(len(Q)+1),r=2)]
    res1 =  list(set(res1))

    res2 =  list(set(res2))

    for i in range(len(res1)):
        a=int(res1[i],2)
        for j in range(len(res2)):
            b = int(res2[j],2)
            xor = a^b
            binary_xor = str(bin(xor).replace("0b",""))

            l = len(binary_xor)
            pow =2**xor
            res = l//pow
            print(binary_xor +"  " + str(xor)+ " "+str(pow)+"  "+ str(res))


            Max=max(Max,res)


    return Max







S="11010"
Q = "111011"

print(MaxVal(S,Q))

