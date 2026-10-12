class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = merged[-1]

            if curr[0] <= prev[1]:
                prev[1] = max(curr[1], prev[1])

            else:
                merged.append(curr)

        return merged