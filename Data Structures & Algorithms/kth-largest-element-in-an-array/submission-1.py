import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        newNums = [0]*len(nums)

        for i in range(len(nums)):
            newNums[i] = -1 * nums[i]

        heapq.heapify(newNums)

        for i in range(k - 1):
            heapq.heappop(newNums)

        return -1 * newNums[0]