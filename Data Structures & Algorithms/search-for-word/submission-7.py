class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, k):
            # k = index in word
            if k == len(word):
                return True
            
            if (i < 0 or i >= rows or 
                j < 0 or j >= cols or 
                board[i][j] != word[k]):
                return False

            # mark visited
            temp = board[i][j]
            board[i][j] = '#'

            # explore neighbors
            found = (
                dfs(i+1, j, k+1) or
                dfs(i-1, j, k+1) or
                dfs(i, j+1, k+1) or
                dfs(i, j-1, k+1)
            )

            # backtrack
            board[i][j] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False