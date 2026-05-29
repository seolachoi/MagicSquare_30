"""UI/API boundary for magic square solver."""

from typing import List, Optional

from boundary.input_validator import InputValidator
from boundary.schemas import (
    BoundaryResponse,
    ErrorDetail,
    FailureResponse,
    SuccessResponse,
)
from control.solve_partial_magic_square import SolvePartialMagicSquare
from entity.exceptions.domain_errors import UnsolvableDomainError


class UIBoundary:
    """Validate input then delegate to control; never throws for contract errors."""

    def __init__(
        self,
        validator: InputValidator | None = None,
        solve_use_case: SolvePartialMagicSquare | None = None,
    ) -> None:
        self._validator = validator or InputValidator()
        self._solve = solve_use_case or SolvePartialMagicSquare()

    def solve(self, grid: Optional[List[List[int]]]) -> BoundaryResponse:
        """Return OK with int[6] or ERROR envelope."""
        failure = self._validator.validate(grid)
        if failure is not None:
            return failure
        assert grid is not None
        try:
            data = self._solve.resolve(grid)
            return SuccessResponse(data=data)
        except UnsolvableDomainError:
            return FailureResponse(
                error=ErrorDetail(
                    code="E006",
                    message="No valid magic square placement.",
                )
            )
