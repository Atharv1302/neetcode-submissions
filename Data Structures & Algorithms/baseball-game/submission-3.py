class Solution:
    def calPoints(self, operations: List[str]) -> int:

        totalScore = 0
        numStack = []

        for op in operations:
            if op == "C":
                totalScore = totalScore - numStack.pop()
            elif op == "D":
                currValue = numStack[-1]
                numStack.append(currValue * 2)
                totalScore = totalScore + (currValue * 2)
            elif op == "+":
                totalScore = totalScore + numStack[-1] + numStack[-2]
                numStack.append(numStack[-1] + numStack[-2])
            else:
                totalScore = totalScore + int(op)
                numStack.append(int(op))
        
        return totalScore

        