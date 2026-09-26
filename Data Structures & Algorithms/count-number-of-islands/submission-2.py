class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        maxCount = 0
        visited = set()
        
        def dfs(row, column):

            nonlocal visited

            if min(row, column) < 0 or column >= len(grid[0]) or row >= len(grid) or (row, column) in visited or grid[row][column] == '0':
                return 

            visited.add((row, column))

            dfs(row + 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)
            dfs(row - 1, column)


        for i in range(0, len(grid), 1):
            for j in range(0, len(grid[0]), 1):
                if grid[i][j] == '1' and not((i, j) in visited):
                    dfs(i, j)
                    maxCount = maxCount + 1
                

        return maxCount


