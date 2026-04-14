class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row, col, visited, prev_height):
            if row < 0 or col < 0:
                return
            if row >= rows or col >= cols:
                return
            if (row, col) in visited:
                return
            if heights[row][col] < prev_height:
                return

            visited.add((row, col))
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])

        for col in range(cols):
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])
        for row in range(rows):
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])

        # intersection
        return [[r, c] for r, c in pacific if (r, c) in atlantic]
