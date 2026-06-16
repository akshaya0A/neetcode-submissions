class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        if len(edges) != n-1:
            return False
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent):
            if node in seen:
                return False
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(seen) == n


       