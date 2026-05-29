"""Locate blank cells (value 0) in row-major order."""

from typing import List, Tuple

from entity.value_objects.constants import GRID_SIZE


class EmptyCellLocator:
    """Find coordinates of cells equal to 0."""

    def locate(self, grid: List[List[int]]) -> List[Tuple[int, int]]:
        """
        Return blank cell coordinates as (row, col) 0-index, row-major.

        Raises:
            ValueError: If blank count is not exactly two.
        """
        blanks: List[Tuple[int, int]] = []
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row][col] == 0:
                    blanks.append((row, col))
        if len(blanks) != 2:
            raise ValueError(f"Expected 2 blanks, found {len(blanks)}")
        return blanks
