class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        occurrence = {}
        for char in s:
            occurrence[char] = occurrence.get(char, 0) + 1

        for char in t:
            if char not in occurrence or occurrence[char] == 0:
                return False
            occurrence[char] -= 1

        return True


        