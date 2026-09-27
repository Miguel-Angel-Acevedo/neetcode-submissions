from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    q = deque()
                    q.append((i, j))
                    grid[i][j] = 0

                    curMax = 1

                    while q:
                        y, x = q.pop()

                        if x > 0 and grid[y][x-1] == 1:
                            curMax += 1
                            grid[y][x-1] = 0
                            q.append((y,x-1))

                        if x < (len(grid[0]))- 1 and grid[y][x+1] ==  1:
                            curMax += 1
                            grid[y][x+1] = 0
                            q.append((y, x+1))

                        if y > 0 and grid[y-1][x] == 1:
                            curMax += 1
                            grid[y-1][x] = 0
                            q.append((y-1,x))

                        if y < (len(grid)) - 1 and grid[y+1][x] ==  1:
                            curMax += 1
                            grid[y+1][x] = 0
                            q.append((y+1, x))

                    maxArea = max(maxArea, curMax)
        return maxArea