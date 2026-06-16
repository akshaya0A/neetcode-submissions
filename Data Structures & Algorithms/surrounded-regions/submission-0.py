from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def dfs(row, col):
            if (
                row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                (row, col) in seen or
                board[row][col] != 'O'
            ):
                return

            seen.add((row, col))
            board[row][col] = '#'

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
