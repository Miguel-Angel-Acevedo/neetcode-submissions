from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        needed = [0] * numCourses
        res = []

        for crs, req in prerequisites:
            graph[req].append(crs)
            needed[crs] += 1

        q = deque()
        for crs in range(numCourses):
            if needed[crs] == 0:
                q.append(crs)

        while q:
            course = q.popleft()
            res.append(course)

            for next_course in graph[course]:
                needed[next_course] -= 1
                if needed[next_course] == 0:
                    q.append(next_course)
        if len(res) != numCourses:
            return []
        return res
