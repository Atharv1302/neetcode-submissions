class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {}

        for i in range(0, len(nums), 1):

            if (target - nums[i]) in store:
                return [store[target - nums[i]], i]
            else:
                store[nums[i]] = i


        