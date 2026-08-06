class Solution:
    def isValid(self, s: str) -> bool:
        
        openBrackets = ["[", "{", "("]
        closeBrackets = {
            "]": "[",
            "}": "{",
            ")": "(",
        }

        bracketStack = []

        for i in range(0, len(s), 1):
            if s[i] in openBrackets:
                bracketStack.append(s[i])
            elif not (not bracketStack) and bracketStack.pop() == closeBrackets[s[i]]:
                continue
            else:
                return False
        
        if not bracketStack:
            return True
        else:
            return False
