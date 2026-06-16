class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        count = 0
        def dfs(node):
            if node in seen: 
                return 
            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        for node in range(n):
            if node not in seen:
                dfs(node)
                count += 1

        return count