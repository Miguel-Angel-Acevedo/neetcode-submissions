class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1 = 0
        rob2 = 0

        for i in range (len(nums)):
            current = nums[i]

            robcur = current + rob1
            skipcur = rob2

            best = max(robcur, skipcur)
            rob1 = rob2
            rob2 = best

        return rob2