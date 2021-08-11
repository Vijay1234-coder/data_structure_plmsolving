l=['a','e','i','o','u']

str = "We work togethere"
str = str.lower()
n=len(str)
for i in range(n):
    if str[i] in l:
        if i!= n-1:
            if str[i+1]==" ":
                print(".",end="")
            else:
                print(str[i+1],end="")
