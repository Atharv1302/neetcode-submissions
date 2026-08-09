class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        store = [0] * (len(nums) + 1)
        ans = []

        for num in nums:
            store[num] = 1

        for i in range(1, len(store), 1):
            if store[i] == 0:
                ans.append(i)

        return ans

        