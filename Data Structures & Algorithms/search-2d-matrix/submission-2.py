class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        leftStart = 0
        RightStart = len(matrix[0]) - 1
        midColumn = 0

        top = 0
        midRow = 0
        bottom = len(matrix) - 1

        if target < matrix[0][0] or target > matrix[bottom][RightStart]:
            return False

        while top <= bottom:

            midRow = int(top + ((bottom - top) / 2))

            if matrix[midRow][0] > target:
                bottom = midRow - 1
            elif matrix[midRow][RightStart] < target:
                top = midRow + 1
            else:
                break

        if not (top <= bottom):
            return False

        while leftStart <= RightStart:

            midColumn = int(leftStart + ((RightStart - leftStart) / 2))

            if matrix[midRow][midColumn] > target:
                RightStart = midColumn - 1
            elif matrix[midRow][midColumn] < target:
                leftStart = midColumn + 1
            else:
                return True

        return False


        