class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()
        DIRECTIONS = [(-1,0), (0, 1), (1, 0), (0, -1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            r, c = queue.popleft()
            current_distance = grid[r][c]

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS:
                    continue
                if nc < 0 or nc >= COLS:
                    continue
                if grid[nr][nc] != INF:
                    continue

                grid[nr][nc] = current_distance + 1
                queue.append((nr, nc))

