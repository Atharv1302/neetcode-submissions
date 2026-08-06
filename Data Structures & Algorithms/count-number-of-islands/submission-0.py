class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()

        ROW, COLUMN = len(grid), len(grid[0])

        def dfs(currentRow, currentColumn):

            if currentRow >= ROW or currentRow < 0 or currentColumn >= COLUMN or currentColumn < 0 or (currentRow, currentColumn) in visited or grid[currentRow][currentColumn] == "0":
                return

            visited.add((currentRow, currentColumn))

            dfs(currentRow + 1, currentColumn)
            dfs(currentRow - 1, currentColumn)
            dfs(currentRow, currentColumn + 1)
            dfs(currentRow, currentColumn - 1)

        islandCount = 0
        for i in range(0, len(grid), 1):
            for j in range(0, len(grid[0]), 1):
                if grid[i][j] == "1" and not ((i, j) in visited):
                    islandCount = 1 + islandCount
                    dfs(i, j)
                    
        return islandCount


            
            
        