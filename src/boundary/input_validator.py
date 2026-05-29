"""Boundary input validation for MagicSquare grid contract."""



from __future__ import annotations



from boundary.schemas import ErrorDetail, FailureResponse

from boundary.validation_result import ValidationResult



_GRID_SIZE = 4

_EXPECTED_EMPTY_CELL_COUNT = 2

_INVALID_SIZE_CODE = "INVALID_SIZE"

_INVALID_SIZE_MESSAGE = "Grid must be 4x4."

_E002_CODE = "E002"

_E002_MESSAGE = "INVALID_EMPTY_COUNT: expected exactly 2 empty cells (0)"

_E004_CODE = "E004"

_E004_MESSAGE = "INVALID_CELL_VALUE: each cell must be 0 or 1..16"

_E005_CODE = "E005"

_E005_MESSAGE = "DUPLICATE_VALUE: non-zero values must be unique"

_MIN_CELL_VALUE = 1

_MAX_CELL_VALUE = 16





class InputValidator:

    """Validates incoming grid input against Boundary contract (E001~E005)."""



    def validate(self, grid: list[list[int]] | None) -> ValidationResult:

        """Validate grid shape and cell values at the Boundary layer.



        Args:

            grid: 4×4 integer matrix, or None when input is absent.



        Returns:

            ``ValidationResult.ok()`` when valid, otherwise ``ValidationResult.error``.

        """

        if grid is None:

            return ValidationResult.from_failure(

                FailureResponse(

                    type="ERROR",

                    error=ErrorDetail(

                        code=_INVALID_SIZE_CODE,

                        message=_INVALID_SIZE_MESSAGE,

                    ),

                )

            )

        if len(grid) != _GRID_SIZE or any(len(row) != _GRID_SIZE for row in grid):

            return ValidationResult.from_failure(

                FailureResponse(

                    type="ERROR",

                    error=ErrorDetail(

                        code=_INVALID_SIZE_CODE,

                        message=_INVALID_SIZE_MESSAGE,

                    ),

                )

            )

        empty_cell_count = sum(cell == 0 for row in grid for cell in row)

        if empty_cell_count != _EXPECTED_EMPTY_CELL_COUNT:

            return ValidationResult.from_failure(

                FailureResponse(

                    type="ERROR",

                    error=ErrorDetail(

                        code=_E002_CODE,

                        message=_E002_MESSAGE,

                    ),

                )

            )

        for row in grid:

            for cell in row:

                if cell != 0 and (

                    cell < _MIN_CELL_VALUE or cell > _MAX_CELL_VALUE

                ):

                    return ValidationResult.from_failure(

                        FailureResponse(

                            type="ERROR",

                            error=ErrorDetail(

                                code=_E004_CODE,

                                message=_E004_MESSAGE,

                            ),

                        )

                    )

        non_zero_values = [cell for row in grid for cell in row if cell != 0]

        if len(non_zero_values) != len(set(non_zero_values)):

            return ValidationResult.from_failure(

                FailureResponse(

                    type="ERROR",

                    error=ErrorDetail(

                        code=_E005_CODE,

                        message=_E005_MESSAGE,

                    ),

                )

            )

        return ValidationResult.ok()

