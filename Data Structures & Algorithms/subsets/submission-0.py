class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(currArray, i):

            if i == len(nums):
                res.append(currArray.copy())
                return

            currArray.append(nums[i])
            dfs(currArray, i + 1)

            currArray.pop()
            dfs(currArray, i + 1)

        dfs([], 0)

        return res


        



        