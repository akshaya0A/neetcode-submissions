class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == ".":
                    continue
                row_key= (row, val)
                col_key = (val, col)
                board_key = (row//3, col//3, val)
                if row_key in seen or col_key in seen or board_key in seen:
                    return False
                else:
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(board_key)
        return True