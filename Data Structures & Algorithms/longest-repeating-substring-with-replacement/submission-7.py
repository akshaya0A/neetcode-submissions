class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longest = 0

        while right < len(s):
            ss = s[left:right + 1]
            counts = Counter(ss)
            lon = max(counts.values())
            width = right - left + 1

            if width - lon <= k:
                longest = max(longest, width)  
                right += 1
            else:
                left += 1

        return longest
