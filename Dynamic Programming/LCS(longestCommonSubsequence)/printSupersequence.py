
''''''
'''IMPORTATNT QUESTION:  '''
def shortestCommonSupersequence(str1,str2):
    t = [[0 for i in range(1002)] for j in range(1002)]
    m = len(str1)
    n = len(str2)

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    r = ""
    result = ""
    i = m
    j = n
    while (i > 0 and j > 0):
        if str1[i - 1] == str2[j - 1]:
            r = r + str1[i - 1]
            i -= 1
            j -= 1
        else:
            if t[i][j - 1] > t[i - 1][j]:
                r = r + str2[j - 1]
                j -= 1
            else:
                r = r + str1[i - 1]    # we took i-1 because string follow zero index notation
                i -= 1


    # here in lcs if either of any sequence becomes zero then we stoped bcz not subsequnce possible but here
    # if any one string become zero it means other string will be supersequence


    while i > 0: # when j==0
        r = r + str1[i - 1]
        i -= 1
    while j > 0: # when i==0 then subsequence will be from j only
        r = r + str2[j - 1]
        j -= 1

    for i in range(len(r) - 1, -1, -1):
        result += r[i]
    return result


str1 = "abac"
str2 = "cab"
print(shortestCommonSupersequence(str1,str2))
