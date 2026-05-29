"""Report/09 Track A — U-OUT-01~03 output contract RED skeleton.

Success int[6] / 1-index / E006 mapping. Control mock 허용 (Dual-Track).
AC-FR05-01~03. Full assert는 Full RED 단계에서 추가.
"""

from __future__ import annotations

from unittest.mock import MagicMock

from boundary.ui_boundary import UIBoundary
from control.solve_partial_magic_square import SolvePartialMagicSquare
from entity.exceptions.domain_errors import UnsolvableDomainError

from tests.conftest import G1_EXPECTED, GRID_G1


class TestSuccessOutputContract:
    """U-OUT-01, U-OUT-02 — 성공 envelope 및 int[6] 1-index."""

    def test_u_out_01_success_returns_int_six_tuple(self) -> None:
        """U-OUT-01, AC-FR05-01 — G1, type OK, Step B placement, len 6."""
        boundary = UIBoundary(solve_use_case=SolvePartialMagicSquare())
        result = boundary.solve(GRID_G1)
        assert result.type == "OK"
        assert result.data == G1_EXPECTED
        assert len(result.data) == 6
        assert "error" not in result.model_dump()

    def test_u_out_02_success_coordinates_are_one_indexed(self) -> None:
        """U-OUT-02, AC-FR05-02 — r,c ∈ [1,4], UX-04."""
        boundary = UIBoundary(solve_use_case=SolvePartialMagicSquare())
        result = boundary.solve(GRID_G1)
        assert result.type == "OK"
        r1, c1, _, r2, c2, _ = result.data
        for coord in (r1, c1, r2, c2):
            assert 1 <= coord <= 4


class TestDomainFailureMapping:
    """U-OUT-03 — UnsolvableDomainError → E006."""

    def test_u_out_03_unsolvable_maps_to_e006(self) -> None:
        """U-OUT-03, AC-FR05-03 — mock UnsolvableDomainError → E006."""
        mock_resolve = MagicMock(spec=SolvePartialMagicSquare)
        mock_resolve.resolve.side_effect = UnsolvableDomainError(
            "No valid magic square completion"
        )
        boundary = UIBoundary(solve_use_case=mock_resolve)
        result = boundary.solve(GRID_G1)
        assert result.type == "ERROR"
        assert result.error.code == "E006"
        assert result.error.message == "UNSOLVABLE: no valid magic square completion"
