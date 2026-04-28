class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        q = deque([])
        fresh_count = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        if fresh_count == 0: return 0

        while q and fresh_count > 0:
            level_size = len(q)
            minutes += 1
            for _ in range(level_size):
                row, col = q.popleft()

                for row_delta, col_delta in DIRECTIONS:
                    next_row = row + row_delta
                    next_col = col + col_delta

                    if next_row < 0 or next_row >= ROWS:
                        continue
                    if next_col < 0 or next_col >= COLS:
                        continue
                    if grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        fresh_count -= 1
                        q.append((next_row, next_col))

        return minutes if fresh_count == 0 else -1