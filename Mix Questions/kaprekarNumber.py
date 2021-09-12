def kaprekarNumbers(p, q):
    lis = []

    for i in range(p, q + 1):

        square = i ** 2
        d = len(str(i))
        string_square = str(square)
        if int(i)==1:
            lis.append(i)
        if len(string_square)>1:
            l_len = len(string_square) - d
            l = string_square[:l_len]
            r = string_square[-d:]
            l = int(l)
            r = int(r)
            if l + r == int(i):
                lis.append(i)
    return lis

print(kaprekarNumbers(1,100))