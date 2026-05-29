"""Validate 4x4 partial magic square input."""

from typing import List, Optional

from boundary.schemas import ErrorDetail, FailureResponse
from entity.value_objects.constants import GRID_SIZE, MAX_VALUE, MIN_VALUE


class InputValidator:
    """Short-circuit validation: null → size → blanks → range → duplicate."""

    def validate(self, grid: Optional[List[List[int]]]) -> FailureResponse | None:
        """
        Return FailureResponse if invalid, else None.

        Order: E003 → E001 → E002 → E004 → E005
        """
        if grid is None:
            return self._fail("E003", "Grid must not be null.")
        if not self._is_4x4(grid):
            return self._fail("E001", "Grid must be 4x4.")
        blank_count = sum(1 for row in grid for v in row if v == 0)
        if blank_count != 2:
            return self._fail("E002", "Grid must contain exactly 2 blank cells (0).")
        for row in grid:
            for value in row:
                if value != 0 and (value < MIN_VALUE or value > MAX_VALUE):
                    return self._fail("E004", f"Value {value} out of range 1..16.")
        non_zero = [v for row in grid for v in row if v != 0]
        if len(non_zero) != len(set(non_zero)):
            return self._fail("E005", "Duplicate non-zero values are not allowed.")
        return None

    @staticmethod
    def _is_4x4(grid: List[List[int]]) -> bool:
        if len(grid) != GRID_SIZE:
            return False
        return all(isinstance(row, list) and len(row) == GRID_SIZE for row in grid)

    @staticmethod
    def _fail(code: str, message: str) -> FailureResponse:
        return FailureResponse(error=ErrorDetail(code=code, message=message))
