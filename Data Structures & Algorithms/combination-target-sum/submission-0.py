class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        solutions = []

        def dfs(index, currentArray, currentTotal):

            if currentTotal == target:
                solutions.append(currentArray.copy())
                return

            if index >= len(nums) or currentTotal > target:
                return

            currentArray.append(nums[index])
            dfs(index, currentArray, currentTotal + nums[index])

            index = index + 1
            currentArray.pop()
            dfs(index, currentArray, currentTotal)

        dfs(0, [], 0)
        return solutions
        