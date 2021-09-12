arr =[1,2,3]
n  = len(arr)
limit = 2**n

for i in range(limit):

    set=""
    temp = i

    for j in range(n-1,-1,-1):
        r = temp % 2
        temp = temp//2
        if r==0:
            set="_"+" "+set
        else:
            set = str(arr[j])+" "+set
    print(set)







