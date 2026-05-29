"""Orchestrate partial magic square solving."""

from typing import List

from entity.exceptions.domain_errors import UnsolvableDomainError
from entity.services.two_cell_solver import TwoCellSolver


class SolvePartialMagicSquare:
    """Control layer use case: validate grid is pre-checked, then solve."""

    def __init__(self, solver: TwoCellSolver | None = None) -> None:
        self._solver = solver or TwoCellSolver()

    def resolve(self, grid: List[List[int]]) -> List[int]:
        """
        Return int[6] solution with 1-index coordinates.

        Raises:
            UnsolvableDomainError: When no valid placement exists.
        """
        return self._solver.solve(grid)
