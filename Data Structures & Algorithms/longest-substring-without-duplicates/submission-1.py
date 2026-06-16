class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = ""
        longest = 0

        for c in s:
            if c not in ss:
                ss += c
            else:
                longest = max(longest, len(ss))
                ss = ss[ss.index(c) + 1:] + c

        return max(longest, len(ss))