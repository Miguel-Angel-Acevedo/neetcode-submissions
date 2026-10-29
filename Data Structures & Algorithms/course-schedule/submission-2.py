
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
        finished = 0

        for crs in range (numCourses):
            if needed[crs] == 0:
                q.append(crs)

        while q:
            crs = q.popleft()
            finished += 1

            for next_course in graph[crs]:
                needed[next_course] -= 1
                if needed[next_course] == 0:
                    q.append(next_course)

        if finished == numCourses:
            return True
        return False