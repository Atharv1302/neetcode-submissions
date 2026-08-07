class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        myStack = []

        for index, height in enumerate(heights):

            startingPoint = index

            while myStack and myStack[-1][1] > height:

                boundLeft, boundHeight = myStack.pop()
                maxArea = max(maxArea, boundHeight * (index - boundLeft))
                startingPoint = boundLeft
            
            myStack.append((startingPoint, height))

        for index, height in myStack:
            maxArea = max(maxArea, height * (len(heights) - index))
        return maxArea