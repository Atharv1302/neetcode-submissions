class Solution:
    def calPoints(self, operations: List[str]) -> int:

        scores = []

        sum = 0
        
        for op in operations:

            if op == "C":
                val = scores.pop()
                sum = sum - val
            elif op == "D":
                currentVal = scores.pop()
                newVal = currentVal*2
                scores.append(currentVal)
                scores.append(newVal)
                sum = sum + newVal
            elif op == "+":
                num1 = scores.pop()
                num2 = scores.pop()
                val = num1 + num2
                scores.append(num2)
                scores.append(num1)
                scores.append(val)
                sum = sum + val
            else:
                val = int(op)
                scores.append(val)
                sum = sum + val

        return sum          