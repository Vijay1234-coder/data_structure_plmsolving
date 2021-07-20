'''important'''
'''ord() convert char to ascii and chr() takes ascii value and convert it into char
upper case letter start from ascci 65 to 90 and lower case start from 97 to 122
 lower to uper add 32 to ascii and if you want to convert lower to upper - 32  '''


s ="aBcDeFgH"
for char in s:
    if ord(char)>=65 and ord(char)<=90:
        s =s.replace(char,chr(ord(char)+32))
print(s)



