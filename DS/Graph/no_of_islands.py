from collections import deque

class Solution:
    def getNeighbours(self, curr, grid, visited):
        neighbours = []
        i, j = curr
        directions=[(-1, 0),(0, -1), (0, 1), (1, 0)]
        for x, y in directions:
            ni, nj = i+x, j+y
            if (0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]=="1" and (ni, nj) not in visited):
                neighbours.append((ni, nj))
        return neighbours

    def numIslands(self, grid):
        count = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i, j) not in visited:
                    count+=1
                    self.traceIsland((i, j), visited, grid)
        return count
        
    def traceIsland(self, source, visited, grid):
        queue = deque([source])
        while (queue):
            curr = queue.popleft()
            if curr not in visited:
                visited.add(curr)
            for neighbour in self.getNeighbours(curr, grid, visited):
                visited.add(neighbour)
                queue.append(neighbour)

soln = Solution()
no = soln.numIslands([
    ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(no)