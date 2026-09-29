class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 or n == 2:
            return n

        cache = {1 : 1, 2: 2}

        def memoization(n, cache):

            if n in cache:
                return cache[n]
            
            cache[n] = memoization((n - 1), cache) + memoization((n-2), cache)

            return cache[n]


        return memoization(n, cache)

        
        