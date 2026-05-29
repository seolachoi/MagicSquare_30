"""Find missing numbers from 1..16 in a partial grid."""

from typing import List, Set

from entity.value_objects.constants import MAX_VALUE, MIN_VALUE


class MissingNumberFinder:
    """Return the two missing values in ascending order."""

    def find(self, grid: List[List[int]]) -> List[int]:
        """List missing integers from MIN_VALUE..MAX_VALUE (excluding 0 cells)."""
        present: Set[int] = set()
        for row in grid:
            for value in row:
                if value != 0:
                    present.add(value)
        missing = [n for n in range(MIN_VALUE, MAX_VALUE + 1) if n not in present]
        if len(missing) != 2:
            raise ValueError(f"Expected 2 missing numbers, found {len(missing)}")
        return sorted(missing)
