class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapp = defaultdict(list)
        for course, pre in prerequisites:
            mapp[course].append(pre)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if mapp[course] == []:
                return True
            visited.add(course)
            for prereq in mapp[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            mapp[course]= []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True