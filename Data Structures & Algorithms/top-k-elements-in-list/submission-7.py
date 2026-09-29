class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[] for i in range (len(nums)+1)]

        for n in nums:
            dic[n] =  1 + dic.get(n, 0)
        for i , n in dic.items():
            freq[n].append(i)

        answer = []

        for j in range (len(freq)-1, -1, -1):
            if not freq[j]:
                continue
            for n in freq[j]:
                answer.append(n)
                k -= 1
                if k == 0:
                    return answer