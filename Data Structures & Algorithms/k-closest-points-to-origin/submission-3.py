import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        myHeap = []

        for i in range(len(points)):
            xValue = points[i][0] 
            yValue = points[i][1] 
            
            dVal = (xValue*xValue) + (yValue*yValue)

            myHeap.append((dVal, xValue, yValue))

        heapq.heapify(myHeap)

        answers = []

        for i in range (0, k, 1):
            d, xVal, yVal = heapq.heappop(myHeap)
            answers.append([xVal, yVal])

        return answers


        
        