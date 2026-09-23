class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, n in enumerate(nums):
            needed = target - n
            if needed in dic:
                return [dic[needed], i]
            
            dic[n] = i
