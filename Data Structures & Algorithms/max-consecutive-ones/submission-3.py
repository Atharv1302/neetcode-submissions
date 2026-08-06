class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxCount = 0
        currentCount = 0

        for num in nums:

            if num == 0:
                currentCount = 0

            else:
                currentCount = currentCount + 1

            if maxCount < currentCount:
                maxCount = currentCount
        
        return maxCount
        