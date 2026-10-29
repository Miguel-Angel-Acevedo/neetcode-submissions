
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        needed = [0] * numCourses

        # Build graph
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            needed[crs] += 1

        # Find courses with no prerequisites
        q = deque()

        for crs in range(numCourses):
            if needed[crs] == 0:
                q.append(crs)

        finished = 0

        # BFS
        while q:
            crs = q.popleft()
            finished += 1

            for next_crs in graph[crs]:
                needed[next_crs] -= 1

                if needed[next_crs] == 0:
                    q.append(next_crs)

        return finished == numCourses
