class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        islands = 0
        
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == '1':
                    islands += 1
                    self.fill(grid, i, j)
                    
        return islands
        
    def fill(self, grid, i, j):
        process = collections.deque()
        grid[i][j] = '0'
        process.append((i, j))
        
        while process:
            r, c = process.popleft()
            adjacent = self.expand(grid, r, c)
            for a, b in adjacent:
                grid[a][b] = '0'
                process.append((a, b))
                
    def expand(self, grid, i, j):
        offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        adjacent = []
        
        for oi, oj in offsets:
            r = i + oi
            c = j + oj
            if r < 0 or r >= len(grid):
                continue
            if c < 0 or c >= len(grid[r]):
                continue
            if grid[r][c] != '1':
                continue
            adjacent.append((r, c))
            
        return adjacent
