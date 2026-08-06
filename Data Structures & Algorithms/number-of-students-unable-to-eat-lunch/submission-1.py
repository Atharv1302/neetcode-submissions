#circular is 0 
#square is 1
from collections import Counter

class Solution:


    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        countDict = Counter(students)

        for sandwich in sandwiches:
            if countDict[sandwich] > 0:
                countDict[sandwich] = countDict[sandwich] - 1
            else:
                break
        
        return countDict[0] + countDict[1]
        