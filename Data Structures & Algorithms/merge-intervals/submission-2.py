class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for i in range (1, len(intervals)):
             current = intervals[i]
             previous = merged[-1]

             if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])

             else:
                merged.append(intervals[i])
                
        return merged