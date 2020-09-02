class Solution:
    def inRange(self, i, j):
        return 0<= i < self.m and 0 <= j < self.n
    
    def cnt(self):
        cnt = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    cnt += 1
                    self.dfs(i, j)
        for i in range(self.m):
            for j in range(self.n):
                self.grid[i][j] = -self.grid[i][j]
        return cnt
                
        
    def dfs(self, i, j):
        self.grid[i][j] = -1
        for k in range(4):
            newX, newY = i + self.dx[k], j + self.dy[k]
            if self.inRange(newX, newY) and self.grid[newX][newY] == 1:
                self.dfs(newX, newY)
                
    def minDays(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
        if self.cnt() > 1:
            return 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self.grid[i][j] = 0
                    if self.cnt() > 1:
                        return 1
                    self.grid[i][j] = 1
        return 2
