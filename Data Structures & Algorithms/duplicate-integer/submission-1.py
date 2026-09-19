class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dictToStore = {}

        for num in nums:
            if num in dictToStore:
                return True
            else:
                dictToStore[num] = 1
        
        return False
        