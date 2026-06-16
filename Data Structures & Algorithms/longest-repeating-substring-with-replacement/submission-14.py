class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        freq = Counter()
        ans = 0 
        for right in range(len(s)):
            freq[s[right]] +=1
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]]-=1
                left +=1
            ans = max(ans, right - left + 1)
        return ans