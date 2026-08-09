class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        maxLength = 0

        indexAppearances = {}

        for i in range(0, len(s), 1):
            if s[i] in indexAppearances and indexAppearances[s[i]] >= left:
                left = indexAppearances[s[i]] + 1

            indexAppearances[s[i]] = i

            maxLength = max(maxLength, i - left + 1)

        return maxLength