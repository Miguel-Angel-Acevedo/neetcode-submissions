class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprof = 0

        while r < len(prices):
            curprof = prices[r] - prices[l]
            maxprof = max(maxprof, curprof)

            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxprof
