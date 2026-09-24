class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxpro = 0


        while r < len(prices):
            if prices[r] > prices[l]:
                maxpro = max(maxpro, prices[r] - prices[l])

            else:
                l = r
            
            r += 1

        return maxpro