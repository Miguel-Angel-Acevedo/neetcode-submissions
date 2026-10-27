from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        fresh = 0
        q = deque()
        minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        while q and fresh > 0:
            for i in range (len(q)):
                y, x = q.popleft()

                if x > 0 and grid[y][x-1] == 1:
                    grid[y][x-1] = 2
                    q.append((y,x-1))
                    fresh -= 1
                if x < len(grid[0])-1 and grid[y][x+1] == 1:
                    grid[y][x+1] = 2
                    q.append((y,x+1))
                    fresh -= 1
                        
                if y > 0 and grid[y-1][x] == 1:
                    grid[y-1][x] = 2
                    q.append((y-1, x))
                    fresh -= 1

                if y < len(grid)-1 and grid[y+1][x] == 1:
                    grid[y+1][x] = 2
                    q.append((y+1,x))
                    fresh -= 1
            minutes += 1
        if fresh >0:
            return -1

        return minutes