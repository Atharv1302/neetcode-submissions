import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        negatedNums = [-s for s in nums]

        heapq.heapify(negatedNums)

        for i in range(0, k-1, 1):
            heapq.heappop(negatedNums)

        return -1 * heapq.heappop(negatedNums)

        