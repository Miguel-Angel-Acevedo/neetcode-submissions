class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[]for i in range(len(nums)+1)]

        for n in nums:
            dic[n] =  1 + dic.get(n, 0)

        for n, c in dic.items():
            freq[c].append(n)

        answer = []

        for c in range (len(freq)-1,-1,-1):
            for n in freq[c]:
                answer.append(n)
                k -= 1
                if k == 0:
                    return answer





