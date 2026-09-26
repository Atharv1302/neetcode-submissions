from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rowLimit, columnLimit = len(grid), len(grid[0])

        rotten = deque()
        freshCount = 0

        for row in range(rowLimit):
            for col in range(columnLimit):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    freshCount += 1
        minute = 0

        while rotten and freshCount > 0:

            for _ in range(len(rotten)):
                rottenRow, rottenColumn = rotten.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
                    tRow, tColumn = rottenRow + dr, rottenColumn + dc

                    if 0 <= tRow < rowLimit and 0 <= tColumn < columnLimit and grid[tRow][tColumn] == 1:
                        grid[tRow][tColumn] = 2
                        rotten.append((tRow, tColumn))
                        freshCount = freshCount - 1

            minute = minute + 1
            
        return -1 if freshCount > 0 else minute

            
        
