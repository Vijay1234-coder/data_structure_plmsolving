'''important'''
'''The Little Elephant loves playing with arrays. He has array a, consisting of n positive integers, indexed from 1 to n. Let's denote the number with index i as ai.

Additionally the Little Elephant has m queries to the array, each query is characterised by a pair of integers lj and rj (1 ≤ lj ≤ rj ≤ n). For each query lj, rj the Little Elephant has to count, how many numbers x exist, such that number x occurs exactly x times among numbers alj, alj + 1, ..., arj.

Help the Little Elephant to count the answers to all queries.

Input
The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 105) — the size of array a and the number of queries to it. The next line contains n space-separated positive integers a1, a2, ..., an (1 ≤ ai ≤ 109). Next m lines contain descriptions of queries, one per line. The j-th of these lines contains the description of the j-th query as two space-separated integers lj and rj (1 ≤ lj ≤ rj ≤ n).

Output
In m lines print m integers — the answers to the queries. The j-th line should contain the answer to the j-th query.

Examples
inputCopy
7 2
3 1 2 2 3 3 7
1 7
3 4
outputCopy
3
1
'''

def helpElephant(arr,queries,q):  #  3 1 2 2 3 3 7
    Ans = [0]*q
    freq =[0]*10000
    queries.sort(key = lambda x:x[1])
    MXN = 10**5 + 5

    currL =0
    currR = -1
    count =0
    idx_lis = [0] * q

    for i in range(q):

        L,R = queries[i]
        idx = origin_index.index([L, R])
        idx_lis[idx]+=1
        if idx_lis[idx]>1:
            idx+=1
        print(idx)



        while(currR<R):
            currR += 1
            if arr[currR]>=MXN:
                return 0
            if freq[arr[currR]] == arr[currR]:
                count-=1
            freq[arr[currR]]+=1
            if freq[arr[currR]] == arr[currR]:
                count+=1


        while (currL > L):
            currL -= 1
            if arr[currL]>=MXN:
                return 0
            if freq[arr[currL]] == arr[currL]:
                count -= 1
            freq[arr[currL]] += 1
            if freq[arr[currL]] == arr[currL]:
                count += 1


        while (currL < L):
            if freq[arr[currL]] == arr[currL]:
                count -= 1
            freq[arr[currL]] -= 1
            if freq[arr[currL]] == arr[currL]:
                count += 1
            currL += 1
        while (currR > R):
            if freq[arr[currR]] == arr[currR]:
                count -= 1
            freq[arr[currR]] -= 1
            if freq[arr[currR]] == arr[currR]:
                count += 1
            currR -= 1
        Ans[idx] = count




    for i in range(len(Ans)) :
        print(Ans[i])

inp = list(map(int,input("n q").split()))
n= inp[0]
q = inp[1]
arr = list(map(int,input("array").split()))
queries = []
origin_index = [0]*q
ans = []
for i in range(q):
    queries.append(list(map(int,input(" query range").split())))
    queries[i][0]-=1
    queries[i][1]-=1
    origin_index[i]=queries[i]

helpElephant(arr,queries,q)






















