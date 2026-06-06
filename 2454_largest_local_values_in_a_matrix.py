class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        result = [[0] * (n-2) for x in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                biggest = 0

                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if biggest < grid[r][c]:
                            biggest = grid[r][c]
                
                result[i][j] = biggest

        return result