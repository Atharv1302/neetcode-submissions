class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROW, COLUMN = len(grid), len(grid[0])

        currentList = set()

        def findIslands(currentRow, currentColumn):

            if currentRow < 0 or currentRow >= ROW or currentColumn < 0 or currentColumn >= COLUMN or (currentRow, currentColumn) in currentList or grid[currentRow][currentColumn] == 0:
                return 0
            
            currentList.add((currentRow, currentColumn))

            return 1 + findIslands(currentRow + 1, currentColumn) + findIslands(currentRow - 1, currentColumn) + findIslands(currentRow, currentColumn + 1) + findIslands(currentRow, currentColumn - 1)

        max_area = 0

        for i in range(0, ROW, 1):
            for j in range(0, COLUMN, 1):
                max_area = max(max_area, findIslands(i, j))

        
        return max_area





            
        