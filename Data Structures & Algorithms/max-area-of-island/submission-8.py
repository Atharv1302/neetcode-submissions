class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        rowLength = len(grid)
        columnLength = len(grid[0])
        maxArea = 0

        def dfs(row, column):

            if not (0 <= row < rowLength) or not (0 <= column < columnLength) or (row, column) in visited or grid[row][column] == 0:
                return 0

            area = 0
            visited.add((row, column))

            area = area + dfs(row + 1, column)
            area = area + dfs(row - 1, column)
            area = area + dfs(row, column + 1)
            area = area + dfs(row, column - 1)

            return 1 + area

        
        for r in range(rowLength):
            for c in range(columnLength):
                if grid[r][c] == 1 and not ((r, c) in visited):
                    curArea = dfs(r, c)
                    maxArea = max(maxArea, curArea)

        return maxArea



            
        