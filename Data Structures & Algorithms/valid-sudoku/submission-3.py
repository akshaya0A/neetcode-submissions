class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        sqaures = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in sqaures[row//3, col//3]):
                    return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                sqaures[(row//3, col//3)].add(board[row][col])
        return True
