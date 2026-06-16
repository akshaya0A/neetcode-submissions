class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, word,0, row, col, seen):
                    return True
        return False
                    
    
    def dfs(self, board, word, i, row, col, seen):
        if i == len(word):
                return True
        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row, col) in seen or board[row][col] != word[i]):
            return False
        seen.add((row,col))
        res = (
                self.dfs(board, word,i + 1, row + 1, col, seen) or
                self.dfs(board, word,i + 1, row - 1, col, seen) or
                self.dfs(board, word, i + 1, row, col + 1,seen) or
                self.dfs(board, word, i + 1, row, col - 1, seen)
            )

        seen.remove((row, col))  
        return res
