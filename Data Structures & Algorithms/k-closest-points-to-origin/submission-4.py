import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        myHeap = []

        for x, y in points:   # instead of indexing
            dVal = x*x + y*y
            myHeap.append((dVal, x, y))

        heapq.heapify(myHeap)

        answers = []

        for i in range (0, k, 1):
            d, xVal, yVal = heapq.heappop(myHeap)
            answers.append([xVal, yVal])

        return answers


        
        