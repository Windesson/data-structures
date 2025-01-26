#https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            nonlocal word, ROWS, COLS, board, path
            
            if i == len(word):
                return True

            if ( (row, col) in path or 
                  min(row, col) < 0 or
                  row >= ROWS or col >= COLS or
                  word[i] != board[row][col] ):
                  return False 

            # visit all 4 direction 
            path.add((row, col))
            res = ( dfs(row, col - 1, i+1) or 
                    dfs(row, col + 1, i+1) or
                    dfs(row -1, col, i+1) or 
                    dfs(row +1, col, i+1) )
        
            path.remove((row, col))
            return res

        for row in range(len(board)):
            for col in range(len(board[row])):
                if dfs(row, col, 0):
                    return True
        return False 

        