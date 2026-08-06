class Solution:
    def rob(self, nums: List[int]) -> int:
        

        money = 0
        totalMax = 0

        for n in nums:
            temp = max(n+money, totalMax)
            money = totalMax
            totalMax = temp
        return totalMax

