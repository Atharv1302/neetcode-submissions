# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        lowerBound = 1
        upperBound = n

        while lowerBound <= upperBound:

            midVal = lowerBound + ((upperBound - lowerBound) // 2)

            guessVal = guess(midVal)

            if guessVal < 0:
                upperBound = midVal - 1
            elif guessVal > 0:
                lowerBound = midVal + 1
            else:
                return midVal
        