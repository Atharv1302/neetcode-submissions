class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0: 
            return False

        parenDict = { '}': '{', ')': '(', ']':'[' }

        trackerStack = []

        for char in s:
            if char in ['[', '{', '(']:
                trackerStack.append(char)

            elif not trackerStack or parenDict[char] != trackerStack.pop():
                return False


        return not trackerStack

        