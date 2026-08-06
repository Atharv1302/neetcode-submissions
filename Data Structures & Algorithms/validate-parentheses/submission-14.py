class Solution:
    def isValid(self, s: str) -> bool:
        
        closeBrackets = {
            "]": "[",
            "}": "{",
            ")": "(",
        }

        bracketStack = []

        for i in range(0, len(s), 1):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                bracketStack.append(s[i])
            elif bracketStack and bracketStack.pop() == closeBrackets[s[i]]:
                continue
            else:
                return False
        
        if not bracketStack:
            return True
        else:
            return False
