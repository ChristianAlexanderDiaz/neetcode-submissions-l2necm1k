class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # pointers at top and bottom for rows
        top = 0
        bottom = len(matrix) - 1

        while (top <= bottom):
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                # target is in this row, second binary search
                l, r = 0, len(matrix[mid]) - 1
                while(l <= r):
                    m = (l + r) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False

        return False



        