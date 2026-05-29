"""Validate complete 4x4 magic square."""

from typing import List

from entity.value_objects.constants import GRID_SIZE, MAGIC_CONSTANT, MAX_VALUE, MIN_VALUE


class MagicSquareValidator:
    """Check row, column, and diagonal sums against MAGIC_CONSTANT."""

    def is_valid_complete(self, grid: List[List[int]]) -> bool:
        """Return True iff grid is 4x4, full (no 0), unique 1..16, all sums match."""
        if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
            return False
        seen: set[int] = set()
        for row in grid:
            for value in row:
                if value == 0 or value < MIN_VALUE or value > MAX_VALUE:
                    return False
                if value in seen:
                    return False
                seen.add(value)
        if len(seen) != MAX_VALUE:
            return False
        return (
            self._all_line_sums_equal(grid)
            and self._diag_sum(grid, 0, 0, 1, 1) == MAGIC_CONSTANT
            and self._diag_sum(grid, 0, GRID_SIZE - 1, 1, -1) == MAGIC_CONSTANT
        )

    def _all_line_sums_equal(self, grid: List[List[int]]) -> bool:
        row_sums = [sum(row) for row in grid]
        if not all(s == MAGIC_CONSTANT for s in row_sums):
            return False
        for col in range(GRID_SIZE):
            if sum(grid[row][col] for row in range(GRID_SIZE)) != MAGIC_CONSTANT:
                return False
        return True

    @staticmethod
    def _diag_sum(
        grid: List[List[int]], start_row: int, start_col: int, dr: int, dc: int
    ) -> int:
        total = 0
        row, col = start_row, start_col
        for _ in range(GRID_SIZE):
            total += grid[row][col]
            row += dr
            col += dc
        return total
