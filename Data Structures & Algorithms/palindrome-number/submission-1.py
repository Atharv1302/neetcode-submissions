class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        while x > reversed_half:
            # Pop the last digit from x and push it into reversed_half
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10
            
        # For even-length numbers: x == reversed_half (e.g., 1221 -> x=12, rev=12)
        # For odd-length numbers: x == reversed_half // 10 (e.g., 12321 -> x=12, rev=123. The middle digit 3 doesn't matter)
        return x == reversed_half or x == reversed_half // 10


        
        