class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            # tuple since list keys cant be mutable
            key = tuple(sorted(s))
            if key not in res:
                res[key] = []
            res[key].append(s)

        return list(res.values())

