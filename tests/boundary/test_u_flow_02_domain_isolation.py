"""Report/09 Track A — U-FLOW-02 Domain isolation RED skeleton (확장).

invalid 입력 시 SolvePartialMagicSquare.resolve() 0회. Control mock/spy 허용.
U-IN-04~08 각 invalid 케이스 확장. AC-FR01-08, BR-05.
"""

from __future__ import annotations

from unittest.mock import MagicMock

from boundary.ui_boundary import UIBoundary
from control.solve_partial_magic_square import SolvePartialMagicSquare

from tests.conftest import GRID_G0


class TestDomainIsolationOnInvalidInput:
    """U-FLOW-02 — invalid 입력 시 resolve() 0회, Failure 반환."""

    def test_u_flow_02_size_violation_execute_never_called(self) -> None:
        """U-FLOW-02, AC-FR01-08 — 3×4 size 위반 → resolve 0회."""
        mock_resolve = MagicMock(spec=SolvePartialMagicSquare)
        boundary = UIBoundary(solve_use_case=mock_resolve)
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        result = boundary.solve(matrix)
        mock_resolve.resolve.assert_not_called()
        assert result.type == "ERROR"

    def test_u_flow_02_u_in_04_zero_empty_execute_never_called(self) -> None:
        """U-FLOW-02 확장, U-IN-04 — G0 빈칸 0개 → resolve 0회."""
        mock_resolve = MagicMock(spec=SolvePartialMagicSquare)
        boundary = UIBoundary(solve_use_case=mock_resolve)
        result = boundary.solve(GRID_G0)
        mock_resolve.resolve.assert_not_called()
        assert result.type == "ERROR"
        assert result.error.code == "E002"

    def test_u_flow_02_u_in_05_three_empty_execute_never_called(self) -> None:
        """U-FLOW-02 확장, U-IN-05 — 빈칸 3개 → resolve 0회."""
        mock_resolve = MagicMock(spec=SolvePartialMagicSquare)
        boundary = UIBoundary(solve_use_case=mock_resolve)
        matrix = [[0, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]
        result = boundary.solve(matrix)
        mock_resolve.resolve.assert_not_called()
        assert result.type == "ERROR"
        assert result.error.code == "E002"

    def test_u_flow_02_u_in_06_minus_one_execute_never_called(self) -> None:
        """U-FLOW-02 확장, U-IN-06 — 셀 -1 → resolve 0회."""
        mock_resolve = MagicMock(spec=SolvePartialMagicSquare)
        boundary = UIBoundary(solve_use_case=mock_resolve)
        matrix = [[16, 3, 2, 13], [-1, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]
        result = boundary.solve(matrix)
        mock_resolve.resolve.assert_not_called()
        assert result.type == "ERROR"
        assert result.error.code == "E004"

    def test_u_flow_02_u_in_07_seventeen_execute_never_called(self) -> None:
        """U-FLOW-02 확장, U-IN-07 — 셀 17 → resolve 0회."""
        mock_resolve = MagicMock(spec=SolvePartialMagicSquare)
        boundary = UIBoundary(solve_use_case=mock_resolve)
        matrix = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 17]]
        result = boundary.solve(matrix)
        mock_resolve.resolve.assert_not_called()
        assert result.type == "ERROR"
        assert result.error.code == "E004"

    def test_u_flow_02_u_in_08_duplicate_execute_never_called(self) -> None:
        """U-FLOW-02 확장, U-IN-08 — non-zero 5 중복 → resolve 0회."""
        mock_resolve = MagicMock(spec=SolvePartialMagicSquare)
        boundary = UIBoundary(solve_use_case=mock_resolve)
        matrix = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 5]]
        result = boundary.solve(matrix)
        mock_resolve.resolve.assert_not_called()
        assert result.type == "ERROR"
        assert result.error.code == "E005"
