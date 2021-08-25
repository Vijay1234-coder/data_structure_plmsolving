s=70
c=0
m =6
for i in range(20,5,-3):
    c+=1
    s =s-i
    if s==0:
        print("count is {} and sum is {}".format(c,s))
        break
    # print(i)
if s!=0:
    x = s//m
    c+=x
print(c)
