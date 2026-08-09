class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)

        trackerStack = []

        for index, temp in enumerate(temperatures):
            while trackerStack and temperatures[trackerStack[-1]] < temp:
                accessIndex = trackerStack.pop()
                ans[accessIndex] = index - accessIndex
            
            trackerStack.append(index)

        return ans

        