class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        

        left = 0
        right = 0

        while right < len(nums):
            if nums[left] != 0:
                left = left + 1
                right = right + 1
            elif nums[right] != 0:
                nums[left] = nums[right]
                nums[right] = 0
                left = left + 1
                right = right + 1
            else:
                right = right + 1
            
        