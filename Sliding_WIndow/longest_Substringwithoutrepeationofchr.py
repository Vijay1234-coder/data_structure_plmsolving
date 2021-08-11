class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        dict = {}
        maxlen = 0
        while j < n:
            if s[j] not in dict:
                dict[s[j]] = 1
            else:
                dict[s[j]] += 1

            if len(dict) == j - i + 1:
                maxlen = max(maxlen, j - i + 1)
                j += 1

            elif len(dict) < j - i + 1:
                while len(dict) < j - i + 1:
                    dict[s[i]] -= 1
                    if dict[s[i]] == 0:
                        dict.pop(s[i])
                    i += 1
                j += 1
        return maxlen

