class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        taking = set()
        taken = set()
        res = []
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        def dfs(course):
            if course in taking:
                return False
            if course in taken:
                return True
            taking.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            taking.remove(course)
            taken.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res