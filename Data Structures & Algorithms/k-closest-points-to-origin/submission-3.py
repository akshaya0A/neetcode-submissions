class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            point = points[i]
            x1 = point[0]
            y1 = point[1]
            dist = x1 * x1 + y1 * y1
            heapq.heappush(heap, (-dist,[x1, y1]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for (_,point) in heap]