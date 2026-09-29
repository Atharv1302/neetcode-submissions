import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        ans = []

        for (x, y) in points:
            dist = (x*x) + (y*y)
            heapq.heappush(ans, (-dist, [x, y]))
            if len(ans) > k:
                heapq.heappop(ans)

        return [point for dist, point in ans]


        
        