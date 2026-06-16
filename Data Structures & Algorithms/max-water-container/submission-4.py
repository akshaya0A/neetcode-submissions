class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0 
        for i in range(len(heights)):
            for h in range(len(heights)):
                height= min(heights[i], heights[h])
                width = h - i
                area = max(area, height*width)
        return area