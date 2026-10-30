
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        needed = [0]*numCourses
        finished = 0

        for cor, pre in prerequisites:
            graph[pre].append(cor)
            needed[cor] += 1


        q = deque()
        for cor in range(numCourses):
            if needed[cor] == 0:
                q.append(cor)

        while q:
            cor = q.popleft()
            finished += 1
            
            for next_course in graph[cor]:
                 needed[next_course] -= 1
                 if needed[next_course] == 0:
                    q.append(next_course)

            if finished == numCourses:
                return True
        return False

