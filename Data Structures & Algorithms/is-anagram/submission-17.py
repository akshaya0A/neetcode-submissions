class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = Counter(s) 
        freq2 = Counter(t)
        for key in freq1:
            if freq1[key] != freq2[key]:
                return False
        return True