class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxtally = 0
        currentTally = 0

        for i in range(0, len(nums), 1):
            if(nums[i] == 1):
                currentTally = currentTally + 1

                if currentTally > maxtally:
                    maxtally = currentTally
            
            else:
                currentTally = 0
        
        return maxtally
        
        