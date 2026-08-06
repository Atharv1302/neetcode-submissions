class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ROW, COLUMN = len(image), len(image[0])
        originalColor = image[sr][sc]

        if originalColor == color:
            return image

        def performFlood(row, column):

            if(min(row, column) < 0 or row > ROW - 1 or column > COLUMN - 1
               or image[row][column] != originalColor):
               return

            image[row][column] = color

            performFlood(row + 1, column)
            performFlood(row - 1, column)
            performFlood(row, column + 1)
            performFlood(row, column - 1)

        performFlood(sr, sc)

        return image

            
        