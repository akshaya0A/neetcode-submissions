class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = set()
        mapp = defaultdict(list)
        for course, prereq in prerequisites:
            mapp[course].append(prereq)
        res =[]
        visited = set()
        def dfs(course):
            if course in seen:
                return False
            if course in visited:
                return True
            seen.add(course)
            for pre in mapp[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res
