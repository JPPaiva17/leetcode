from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        columns = len(grid[0])
        counter = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] > 0:
                    queue = deque([(i,j)])
                    islandSum = grid[i][j]
                    grid[i][j] = 0

                    while queue:
                        x, y = queue.popleft()

                        if x-1 >= 0 and grid[x-1][y] > 0:
                            islandSum += grid[x-1][y]
                            grid[x-1][y] = 0
                            queue.append((x-1,y))

                        if x+1 < rows and grid[x+1][y] > 0:
                            islandSum += grid[x+1][y]
                            grid[x+1][y] = 0
                            queue.append((x+1,y))
                        
                        if y - 1 >= 0 and grid[x][y-1] > 0:
                            islandSum += grid[x][y-1]
                            grid[x][y-1] = 0
                            queue.append((x, y-1))

                        if y + 1 < columns and grid[x][y+1] > 0:
                            islandSum += grid[x][y+1]
                            grid[x][y+1] = 0
                            queue.append((x, y+1))
                        
                    if islandSum%k == 0:
                        counter +=1

        return counter