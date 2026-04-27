class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            current_distance = grid[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows:
                    continue
                if nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] != INF:
                    continue
                
                grid[nr][nc] = current_distance + 1
                queue.append((nr, nc))