"""Use case orchestrator for partial magic square solving."""

from __future__ import annotations

from entity.services.two_cell_solver import TwoCellSolver


class SolvePartialMagicSquare:
    """Orchestrates two-cell solve for a validated 4×4 grid."""

    def __init__(self, two_cell_solver: TwoCellSolver | None = None) -> None:
        """Initialize use case with injectable domain solver.

        Args:
            two_cell_solver: Attempts Step A/B completion and validation.
        """
        self._two_cell_solver = two_cell_solver or TwoCellSolver()

    def resolve(self, grid: list[list[int]]) -> list[int]:
        """Run domain solve and return ``int[6]`` for a valid grid.

        Args:
            grid: Validated 4×4 integer matrix with exactly two empty cells.

        Returns:
            Six-element result ``[r1, c1, n1, r2, c2, n2]`` (1-index).

        Raises:
            UnsolvableDomainError: When the domain solver finds no completion.
        """
        return self._two_cell_solver.solve(grid).values
