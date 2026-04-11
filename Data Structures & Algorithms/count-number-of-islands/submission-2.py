class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        visited = set()
        

        def dfs(grid, row, col, visited):
            if row < 0 or col < 0:
                return
            if row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in visited:
                return
            if grid[row][col] == '0':
                return
            
            visited.add((row, col))
            dfs(grid, row - 1, col, visited)
            dfs(grid, row , col + 1, visited)
            dfs(grid, row + 1, col, visited)
            dfs(grid, row, col - 1, visited)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(grid, row, col, visited)
                    self.count += 1

        return self.count