class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}

        for n in nums:
            seen[n] = 1 + seen.get(n, 0)
        return max(seen, key=seen.get)
