from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh = 0
        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:

            for i in range(len(q)):
                y, x = q.popleft()

                # Left
                if x > 0 and grid[y][x-1] == 1:
                    grid[y][x-1] = 2
                    q.append((y, x-1))
                    fresh -= 1

                # Right
                if x < cols-1 and grid[y][x+1] == 1:
                    grid[y][x+1] = 2
                    q.append((y, x+1))
                    fresh -= 1

                # Up
                if y > 0 and grid[y-1][x] == 1:
                    grid[y-1][x] = 2
                    q.append((y-1, x))
                    fresh -= 1

                # Down
                if y < rows-1 and grid[y+1][x] == 1:
                    grid[y+1][x] = 2
                    q.append((y+1, x))
                    fresh -= 1

            minutes += 1

        if fresh > 0:
            return -1

        return minutes