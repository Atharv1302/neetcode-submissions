import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        my_dict = []

        for i in range(len(points)):
            xValue = points[i][0] 
            yValue = points[i][1] 
            
            dVal = math.sqrt((xValue*xValue) + (yValue*yValue))

            my_dict.append((points[i], dVal))

        sorted_list = sorted(my_dict, key=lambda item: item[1])
        return [item[0] for item in sorted_list[:k]]
        