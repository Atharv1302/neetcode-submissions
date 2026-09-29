class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 or n == 2:
            return n

        cache = {1 : 1, 2: 2}

        def memoization(n, cache):

            val = 0

            if n in cache:
                return cache[n]
            
            else:
                val = memoization((n - 1), cache) + memoization((n-2), cache)

            cache[n] = cache.get(n, 0) + val

            return val


        return memoization(n, cache)

            
        
        