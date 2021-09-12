arr= [1,2,"AJAY",5,10,"VIJAY"]
even =[]
odd = []
string =[]
for x in arr:
    try:
        if x%1==0:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
    except:
        string.append(x)
print("Even:" , even)
print("odd: ",odd)
print("string: ",string)