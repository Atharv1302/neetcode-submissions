#circular is 0 
#square is 1

class Solution:


    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        unableToEat = 0

        while(unableToEat < len(students)):

            if(students[0] == sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
                unableToEat = 0
            else:
                students.append(students.pop(0))
                unableToEat = unableToEat + 1

        return unableToEat
        