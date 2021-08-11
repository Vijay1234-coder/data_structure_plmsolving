def reverse_word(s):
    i =0
    j =0
    lis =[]

    while i<len(s):
       if s[i]!=" ":
           start = i
       while(i < len(s) and s[i]!=" "):
           i+=1
       lis.append(s[start:i])

       i += 1
    return lis








print(reverse_word("this is vijay singh"))