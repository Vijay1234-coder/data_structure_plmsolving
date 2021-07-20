n =3
r = ""
for i in range(4):
    while n>0:
        d = n%2
        n= n//2
        r =str(d) + r

print(r)