class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        myStack = []

        for index, height in enumerate(heights + [0]):
            while myStack and height < heights[myStack[-1]]:
                poppedIndex = myStack.pop()
                width = index if not myStack else index - myStack[-1] - 1
                maxArea = max(maxArea, heights[poppedIndex] * width)

            myStack.append(index)


        return maxArea