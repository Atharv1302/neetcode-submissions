class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxTally = 0
        currentTally = 0

        for num in nums:

            if num == 1:
                currentTally = currentTally + 1

                if currentTally > maxTally:
                    maxTally = currentTally
            
            else:
                currentTally = 0
        
        return maxTally
        
        