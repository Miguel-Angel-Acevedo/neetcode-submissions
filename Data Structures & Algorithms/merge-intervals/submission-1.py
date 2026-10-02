class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])

        answer = [intervals[0]]

        for start, end in intervals[1:]:
            lastend = answer[-1][1]

            if start <= lastend:
                answer[-1][1] = max(lastend, end)
            else:
                answer.append([start,end])
        return answer