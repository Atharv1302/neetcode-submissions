class Solution:
    def sortColors(self, nums: List[int]) -> None:

        myDict = {0: 0, 1: 0, 2: 0}

        for num in nums:
            myDict[num] = myDict[num] + 1

        i = 0

        for j in range(3):
            for k in range (myDict[j]):
                nums[i] = j
                i = i + 1
        