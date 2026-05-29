"""Report/09 Track B — D-VAL-01~06 magic square validator RED skeleton.

완전 격자 I1~I5 검증. Domain Mock 금지. AC-FR04-*.
"""

from __future__ import annotations

import copy

from entity.services.magic_square_validator import MagicSquareValidator

from tests.conftest import GRID_G0


class TestMagicSquareValidatorComplete:
    """D-VAL-01 — G0 완전 격자 → true."""

    def test_d_val_01_g0_complete_grid_returns_true(self) -> None:
        """D-VAL-01, I1~I5 — G0 is_valid_complete → True."""
        validator = MagicSquareValidator()
        assert validator.is_valid_complete(GRID_G0) is True


class TestMagicSquareValidatorRowSum:
    """D-VAL-02 — 행 합 불일치 → false."""

    def test_d_val_02_row_sum_mismatch_returns_false(self) -> None:
        """D-VAL-02, I1 — G0 row0 sum broken → False."""
        validator = MagicSquareValidator()
        modified = copy.deepcopy(GRID_G0)
        modified[0][0], modified[1][0] = modified[1][0], modified[0][0]
        assert validator.is_valid_complete(modified) is False


class TestMagicSquareValidatorColSum:
    """D-VAL-03 — 열 합 불일치 → false."""

    def test_d_val_03_col_sum_mismatch_returns_false(self) -> None:
        """D-VAL-03, I2 — G0 column sum broken → False."""
        validator = MagicSquareValidator()
        modified = copy.deepcopy(GRID_G0)
        modified[0][1], modified[1][1] = modified[1][1], modified[0][1]
        assert validator.is_valid_complete(modified) is False


class TestMagicSquareValidatorDiagonal:
    """D-VAL-04 — 대각 불일치 → false."""

    def test_d_val_04_diagonal_mismatch_returns_false(self) -> None:
        """D-VAL-04, I3 — G0 main diagonal broken → False."""
        validator = MagicSquareValidator()
        modified = copy.deepcopy(GRID_G0)
        modified[0][0], modified[3][3] = modified[3][3], modified[0][0]
        assert validator.is_valid_complete(modified) is False


class TestMagicSquareValidatorDuplicate:
    """D-VAL-05 — 1~16 중복 → false."""

    def test_d_val_05_duplicate_values_returns_false(self) -> None:
        """D-VAL-05, I4 — duplicate value in complete grid → False."""
        validator = MagicSquareValidator()
        modified = copy.deepcopy(GRID_G0)
        modified[1][0] = modified[0][1]
        assert validator.is_valid_complete(modified) is False


class TestMagicSquareValidatorZeroCell:
    """D-VAL-06 — 0 포함 → false."""

    def test_d_val_06_zero_cell_returns_false(self) -> None:
        """D-VAL-06, I4 — complete grid with zero cell → False."""
        validator = MagicSquareValidator()
        grid_with_zero = copy.deepcopy(GRID_G0)
        grid_with_zero[0][0] = 0
        assert validator.is_valid_complete(grid_with_zero) is False
