"""UIBoundary — orchestrates input validation and Control use-case calls."""

from __future__ import annotations

from boundary.error_mapper import ErrorMapper
from boundary.input_validator import InputValidator
from boundary.schemas import FailureResponse, SuccessResponse
from control.solve_partial_magic_square import SolvePartialMagicSquare


class UIBoundary:
    """Boundary entry point for solving a partial magic square from UI/API."""

    def __init__(
        self,
        solve_use_case: SolvePartialMagicSquare,
        input_validator: InputValidator | None = None,
        error_mapper: ErrorMapper | None = None,
    ) -> None:
        """Initialize UIBoundary with injected Control and optional validator.

        Args:
            solve_use_case: Control use case invoked only after validation passes.
            input_validator: Boundary validator; defaults to ``InputValidator()``.
            error_mapper: Domain → Boundary error translator; defaults to new instance.
        """
        self._solve_use_case = solve_use_case
        self._input_validator = input_validator or InputValidator()
        self._error_mapper = error_mapper or ErrorMapper()

    def solve(
        self, grid: list[list[int]] | None
    ) -> FailureResponse | SuccessResponse:
        """Validate input and delegate to Control when validation succeeds.

        Args:
            grid: 4×4 integer matrix, or None when input is absent.

        Returns:
            FailureResponse when input validation fails, otherwise SuccessResponse.
        """
        validation = self._input_validator.validate(grid)
        if validation.is_error:
            assert validation.failure is not None
            return validation.failure

        try:
            data = self._solve_use_case.resolve(grid)  # type: ignore[arg-type]
        except Exception as exc:
            return self._error_mapper.map_domain_error(exc)
        return SuccessResponse(type="OK", data=data)
