


def reverse(s):


    if len(s)<= 1:
        return s
    else:
        return reverse(s[1:])+s[0]   # 'bc'+'a'
                                     #'c'+'b'+'a'







print(reverse('abc'))
