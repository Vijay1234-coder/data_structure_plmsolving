# from itertools import *
#
#
#
# def permute(s):
#     res=[]
#     for i in permutations(s):
#         v="".join(i)
#         res.append(v)
#     return res
#
#
#
# print(permute("aaa"))



'''..................... by using recurssion  ............................'''


'''
String Permutation
Problem Statement
Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'

Algorithm:--
Let's think about what the steps we need to take here are:

Iterate through the initial string – e.g., ‘abc’.
For each character in the initial string, set aside that character and get a list of all permutations of the string that’s left. So, for example, if the current iteration is on 'b', we’d want to find all the permutations of the string 'ac'.

Once you have the list from step 2, add each element from that list to the character from the initial string, and append the result to our list of final results. So if we’re on 'b' and we’ve gotten the list ['ac', 'ca'], we’d add 'b' to those, resulting in 'bac' and 'bca', each of which we’d add to our final results.

Return the list of final results.

Let's go ahead and see this implemented:'''


# def permute(s):
#     out = []
#
#     # Base Case
#     if len(s) == 1:
#         out = [s]
#
#     else:
#         # For every letter in string
#         for i, let in enumerate(s):
#
#
#             # For every permutation resulting from Step 2 and 3 described above
#             for perm in permute(s[:i] + s[i + 1:]):
#
#                 # Add it to output
#                 out += [let + perm]
#
#     return out
#
#
# print(permute('abc'))


def permute(s,i):
    if i==len(s)-1:
        print("".join(s))

    else:
        for j in range(i,len(s)):


            s[i],s[j] = s[j],s[i]
            permute(s,i+1)
            s[i],s[j] = s[j],s[i]
string = "abc"
str = list(string)
permute(str,0)


