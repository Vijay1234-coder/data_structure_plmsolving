n =17
s=""
while n > 0:
    rem = n % 2
    s = str(rem) + s
    n =n//2
print(s)

print("------DECIMAL TO BINARY_____________")
stri =list(s)
deci = 0
for i in range(len(stri)):

    binary =stri.pop()
    if binary=='1':
        deci+=2**i
print(deci)




