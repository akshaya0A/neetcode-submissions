class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area =0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = max(area, self.helper(grid, row, col))
        return area

    def helper(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        count = 1
        grid[row][col] = 0
        count += self.helper(grid, row+1, col)
        count += self.helper(grid, row-1, col)
        count += self.helper(grid, row, col+1)
        count += self.helper(grid, row, col-1)
        return count
