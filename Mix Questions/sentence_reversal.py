'''below method is just for showing that you know python but never use this method in interview'''
# x=input("enter any string")
# y=x.strip().split(" ")
# z=" ".join(reversed(y))
# print(z)
def Reverse_sentance(s):
    space_list = [" "]
    store_list = []
    length = len(s)
    reverse_stringlis = []
    i = 0

    while (i < length):
        if (s[i] not in space_list):
            start_word = i
            while i < length and s[i] not in space_list:
                i += 1
            store_list.append(s[start_word:i])

        i += 1
                                               # ''' rahther than using above loop we also do as follow '''

    for j in range(len(store_list)):
        j+=1
        reverse_stringlis.append(store_list[-j])


    return " ".join(reverse_stringlis)

#  return " ".join(reversed(store_list))






print(Reverse_sentance(input("enter your string")))






