
''''''
'''LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.
x:"ABCDGH"
y:"AEDFHR"
o/p: 4 explaination: “ADH”      '''


def lcs(x,y,n,m):
    # Base Case
    if n==0 or m==0:
        return 0
    if (x[n-1]==y[m-1]):
        return 1+lcs(x,y,n-1,m-1)
    else:
        return max(lcs(x,y,n-1,m),lcs(x,y,n,m-1))





x= "AGGTAB"
y= "GXTXAYB"
n=len(x)
m=len(y)
print(lcs(x,y,n,m))
