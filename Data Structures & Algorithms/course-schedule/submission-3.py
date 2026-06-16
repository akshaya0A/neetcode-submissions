class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taking = set()  
        taken = set()   
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        def dfs(course):
            if course in taking:  
                return False
            if course in taken:   
                return True

            taking.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            taking.remove(course)
            taken.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True


