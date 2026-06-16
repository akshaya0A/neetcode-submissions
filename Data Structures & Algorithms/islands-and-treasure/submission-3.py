class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        self.visit = set()
        self.q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    self.q.append((r, c))
                    self.visit.add((r, c))

        dist = 0
        while self.q:
            for _ in range(len(self.q)):
                r, c = self.q.popleft()
                grid[r][c] = dist
                self.addCell(grid, r + 1, c)
                self.addCell(grid, r - 1, c)
                self.addCell(grid, r, c + 1)
                self.addCell(grid, r, c - 1)
            dist += 1

    def addCell(self, grid, r, c):
        if (min(r, c) < 0 or r == len(grid) or c == len(grid[0]) or
            (r, c) in self.visit or grid[r][c] == -1):
            return
        self.visit.add((r, c))
        self.q.append((r, c))
