class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones)
            seccond = heapq.heappop(stones)

            if seccond > first:
                heapq.heappush(stones, first - seccond)
        stones.append(0)
        return abs(stones[0])

