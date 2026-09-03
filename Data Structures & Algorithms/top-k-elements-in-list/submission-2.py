nums = [1,2,3,1,2,3,3]
count = {1:2, 2:2, 3:3}
freq = [[],[],[1, 2],[3],[],[],[],[]]
res = [3, 2]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) -1, -1,-1):
            for a in freq[i]:
                res.append(a)
                k -= 1

                if k <= 0:
                    return res
