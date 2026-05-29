"""Solve partial magic square with exactly two blanks."""

from copy import deepcopy
from typing import List, Tuple

from entity.exceptions.domain_errors import UnsolvableDomainError
from entity.services.empty_cell_locator import EmptyCellLocator
from entity.services.magic_square_validator import MagicSquareValidator
from entity.services.missing_number_finder import MissingNumberFinder


class TwoCellSolver:
    """Try small-first then reverse placement; return 1-index int[6]."""

    def __init__(self) -> None:
        self._locator = EmptyCellLocator()
        self._finder = MissingNumberFinder()
        self._validator = MagicSquareValidator()

    def solve(self, grid: List[List[int]]) -> List[int]:
        """
        Return [r1, c1, n1, r2, c2, n2] with 1-index coordinates.

        Raises:
            UnsolvableDomainError: If neither placement works.
        """
        blanks = self._locator.locate(grid)
        smaller, larger = self._finder.find(grid)
        (r1, c1), (r2, c2) = blanks[0], blanks[1]

        for n1, n2 in ((smaller, larger), (larger, smaller)):
            trial = deepcopy(grid)
            trial[r1][c1] = n1
            trial[r2][c2] = n2
            if self._validator.is_valid_complete(trial):
                return [r1 + 1, c1 + 1, n1, r2 + 1, c2 + 1, n2]

        raise UnsolvableDomainError()
