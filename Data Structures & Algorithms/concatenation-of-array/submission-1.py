class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        newNums = [None] * 2 * len(nums)

        for i in range(0, len(nums), 1):
            newNums[i] = nums[i]
            newNums[i + (len(nums))] = nums[i]

        return newNums

        