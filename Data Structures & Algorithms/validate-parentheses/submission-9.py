class Solution:
    def isValid(self, s: str) -> bool:

        bracketDict = {'(' : ')', '{' : '}','[' : ']'}
        endStack = []

        for char in s:
            if char in bracketDict:
                endStack.append(bracketDict[char])
            elif not endStack or endStack.pop() != char:
                return False

        return not endStack
             

            
        