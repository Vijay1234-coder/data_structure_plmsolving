#https://leetcode.com/contest/weekly-contest-253/problems/minimum-number-of-swaps-to-make-the-string-balanced/
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if stack == []:
                stack.append(s[i])
            else:
                if s[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(s[i])

                else:
                    stack.append(s[i])

        if len(stack) % 4 == 0: # if we balance any two bracket lits will balance 4 bracket
            x = 0
        if len(stack) % 4 == 2:#else left with two
            x = 1
        res = len(stack) // 4 + x
        return res
