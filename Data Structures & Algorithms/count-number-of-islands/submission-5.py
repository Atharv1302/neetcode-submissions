class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        visited = set()
        rowWidth = len(grid)
        columnWidth = len(grid[0])
        islandCount = 0

        def dfs(row, column):

            if not (0 <= row < rowWidth) or not(0 <= column < columnWidth) or grid[row][column] == "0" or (row, column) in visited:
                return

            visited.add((row, column))

            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

        
        for r in range(rowWidth):
            for c in range(columnWidth):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islandCount += 1
        
        return islandCount

