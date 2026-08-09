class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        myStack = []

        heights = heights + [0]

        for index, height in enumerate(heights):

            while myStack and heights[myStack[-1]] > height:

                poppedIndex = myStack.pop()

                width = index if not myStack else index - myStack[-1] - 1

                maxArea = max(maxArea, heights[poppedIndex] * width)

            myStack.append(index)

        return maxArea