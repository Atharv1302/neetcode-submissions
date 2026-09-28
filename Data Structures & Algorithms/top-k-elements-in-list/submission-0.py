from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictV = Counter(nums)

        mostCommon = dictV.most_common(k)

        ans = []

        for key, value in mostCommon:
            ans.append(key)

        return ans

        