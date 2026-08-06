class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 or n==2 or n==3:
            return n
        
        n1, n2 = 2, 3

        for i in range (4, n+1):

            curr = n1 + n2
            n1 = n2
            n2 = curr
        
        return n2

        
        