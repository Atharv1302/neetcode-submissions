class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mySet = set(nums)
        maxLength = 0

        for num in mySet:

            if not (num - 1 in mySet):

                length = 1

                while (num) + length in mySet:
                    length = length + 1

                maxLength = max(length, maxLength)

        return maxLength