# # ''' if string is unique return true else false eg "abcd" return true else "aabbcd" return false'''
# # method 1: but dont use in interview
# def unique_char1(s):
#     return len(set(s))==len(s)
#
#
# print(unique_char1("abc"))
#
# # method 2: use this in interview highly recomended in order to show that you know algo
#
# def unique_char2(s):
#     val = set()
#     for char in s:
#         if char in val:
#             return False
#         else:
#             val.add(char)
#     return True
# print(unique_char2("abccc"))
#
#
#
#
