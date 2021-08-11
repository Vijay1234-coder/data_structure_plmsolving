'''Anagram --  if any sring having different meaning of word but using same char then it is anagram
for example god and dog are anagram '''


'''write  code in which  if u give any two string it will return true if it is anagram false if it is not'''

def anagram1(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False

    count = {}
    for letter in s1:
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1

    for letter in s2:
        if letter in count:
            count[letter]-=1
        else:
            count[letter]=1
    for k in count:
        if count[k]!= 0:
            return False
    print(True)

anagram1('dogs','god')
