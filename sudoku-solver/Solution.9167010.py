class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    
    def dfs(self, board, rows, cols, grids, num):
        if num == 81:
            return True
            
        i = num / 9
        j = num % 9
            
        if board[i][j] != '.':
            return self.dfs(board, rows, cols, grids, num + 1)
            
        for d in xrange(1, 10):
            if rows[i][d - 1]:
                continue
            if cols[j][d - 1]:
                continue
            if grids[i / 3][j / 3][d - 1]:
                continue
            
            rows[i][d - 1] = True
            cols[j][d - 1] = True
            grids[i / 3][j / 3][d - 1] = True
            board[i][j] = str(d)
            
            result = self.dfs(board, rows, cols, grids, num + 1)
            if result:
                return True
            
            rows[i][d - 1] = False
            cols[j][d - 1] = False
            grids[i / 3][j / 3][d - 1] = False
            board[i][j] = '.'
            
        return False


    def solveSudoku(self, board):
        rows = [[False] * 9 for _ in xrange(9)]
        cols = [[False] * 9 for _ in xrange(9)]
        grids = [[[False] * 9 for _ in xrange(3)] for _ in xrange(3)]
        
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                rows[i][num - 1] = True
                cols[j][num - 1] = True
                grids[i / 3][j / 3][num - 1] = True
                
        self.dfs(board, rows, cols, grids, 0)
