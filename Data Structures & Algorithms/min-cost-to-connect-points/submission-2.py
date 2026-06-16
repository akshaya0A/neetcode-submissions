class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                cost = abs(x2-x1) + abs(y2-y1)
                graph[i].append((cost, j))
                graph[j].append((cost, i))
        
        minheap = [(0,0)]
        total= 0
        seen = set()

        while len(seen) < len(points):
            w, p = heapq.heappop(minheap)
            if p in seen:
                continue
            total += w
            seen.add(p)
            for c2, p2 in graph[p]:
                if p2 not in seen:
                    heapq.heappush(minheap, (c2, p2))
        return total
