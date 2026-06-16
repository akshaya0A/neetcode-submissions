class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count = 0
        seen = set()
        def dfs(edge):
            if edge in seen:
                return False
            seen.add(edge)
            for neighbor in graph[edge]:
                dfs(neighbor)
        for e in range(n):
            if e not in seen:
                dfs(e)
                count +=1
        return count