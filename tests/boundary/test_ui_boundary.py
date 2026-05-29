"""UIBoundary integration tests — Track A."""

from unittest.mock import MagicMock

import pytest

from boundary.schemas import SuccessResponse
from boundary.ui_boundary import UIBoundary
from control.solve_partial_magic_square import SolvePartialMagicSquare
from entity.exceptions.domain_errors import UnsolvableDomainError
from tests.conftest import G1_EXPECTED


def test_none_grid_resolve_never_called() -> None:
    mock_uc = MagicMock(spec=SolvePartialMagicSquare)
    boundary = UIBoundary(solve_use_case=mock_uc)
    result = boundary.solve(None)
    assert result.type == "ERROR"
    assert result.error.code == "E003"
    mock_uc.resolve.assert_not_called()


def test_g1_success_int_six(grid_g1: list[list[int]]) -> None:
    boundary = UIBoundary()
    result = boundary.solve(grid_g1)
    assert isinstance(result, SuccessResponse)
    assert result.data == G1_EXPECTED
    assert len(result.data) == 6


def test_unsolvable_returns_e006(grid_g1: list[list[int]]) -> None:
    mock_uc = MagicMock(spec=SolvePartialMagicSquare)
    mock_uc.resolve.side_effect = UnsolvableDomainError()
    boundary = UIBoundary(solve_use_case=mock_uc)
    result = boundary.solve(grid_g1)
    assert result.type == "ERROR"
    assert result.error.code == "E006"
