class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0

        for r in range(nr):
            for c in range(nc):
                if(grid[r][c] == '1' ):
                    num_islands += 1
                    self.dfs(grid, r, c)
        
        return num_islands
        
    
    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])

        if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'

        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)