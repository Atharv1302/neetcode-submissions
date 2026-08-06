class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        right = len(arr) - 1

        max = arr[right]

        while (right - 1) >= 0:

            if arr[right - 1] > max:
                temp = arr[right - 1]
                arr[right - 1] = max
                max = temp
            else:
                arr[right - 1] = max
            
            right = right - 1

        arr[len(arr) - 1] = -1

        return arr
        