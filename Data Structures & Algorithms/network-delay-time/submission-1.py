class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        heap = [[0, k]]
        distance = {}
        while heap:
            time, node = heapq.heappop(heap)
            if node in distance:
                continue
            distance[node] =time
            for neighbor, w in graph[node]:
                if neighbor not in distance:
                    heapq.heappush(heap, (time + w, neighbor))
        if len(distance) != n:
            return -1
        return max(distance.values())
