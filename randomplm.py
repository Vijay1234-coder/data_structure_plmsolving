p=[1,2,3,4]
q=[1,3,4,5]
k=4
l=[]
for _ in range(10001):
    p.append(0)
for num in q:
    if num in p:
        indx = p.index(num)+k-1
        if p[indx] in p :
            l.append(p[indx])
    else:l.append(0)

print(l)


