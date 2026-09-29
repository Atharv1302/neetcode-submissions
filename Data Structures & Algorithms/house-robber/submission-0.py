class Solution:
    def rob(self, nums: List[int]) -> int:
        
        ansForOdd = 0
        ansForEven = 0


        for i in range(0, len(nums), 1):

            if i % 2 == 0:
                ansForEven = max(ansForOdd, ansForEven + nums[i])
            else:
                ansForOdd = max(ansForEven, ansForOdd + nums[i])

        return max(ansForOdd, ansForEven)
