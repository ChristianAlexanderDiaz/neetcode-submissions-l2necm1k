class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        visited = set()

        def dfs(grid, row, col, visited):
            if row < 0 or col < 0:
                return 0
            if row >= len(grid) or col >= len(grid[0]):
                return 0
            if (row, col) in visited:
                return 0
            if grid[row][col] == 0:
                return 0

            visited.add((row, col))
            return (1 + dfs(grid, row - 1, col, visited) +
            dfs(grid, row + 1, col, visited) +
            dfs(grid, row , col + 1, visited) +
            dfs(grid, row, col - 1, visited))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    self.maxArea = max(self.maxArea, dfs(grid, row, col, visited))
        
        return self.maxArea