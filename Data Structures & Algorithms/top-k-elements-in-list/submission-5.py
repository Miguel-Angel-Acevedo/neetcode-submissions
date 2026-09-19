nums = [1,2,3,1,2,3,3]
count = {1:2, 2:2, 3:3}
freq = [[],[],[1, 2],[3],[],[],[],[]]
res = [3, 2]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[]for i in range (len(nums) +1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        answer = []

        for i in range(len(freq) -1, 0,-1):
            for n in freq[i]:
                answer.append(n)
                k -= 1
                if k == 0:
                    return answer