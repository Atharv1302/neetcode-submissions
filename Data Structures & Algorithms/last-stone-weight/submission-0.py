class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python has min-heap, so negate weights to simulate max-heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)  # heaviest (most negative)
            y = heapq.heappop(stones)  # second heaviest

            if x != y:
                # x is "smaller" because negative, e.g. -6 vs -4
                # new weight is abs(x) - abs(y) => x - y (negative)
                heapq.heappush(stones, x - y)

        # If no stones remain, return 0
        return abs(stones[0]) if stones else 0