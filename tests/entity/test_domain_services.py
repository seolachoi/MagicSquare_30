"""Domain logic tests — Track B."""

import pytest

from entity.exceptions.domain_errors import UnsolvableDomainError
from entity.services.empty_cell_locator import EmptyCellLocator
from entity.services.magic_square_validator import MagicSquareValidator
from entity.services.missing_number_finder import MissingNumberFinder
from entity.services.two_cell_solver import TwoCellSolver
from entity.value_objects.constants import MAGIC_CONSTANT
from tests.conftest import G1_EXPECTED, GRID_G1


def test_locate_blanks_row_major_g1() -> None:
    locator = EmptyCellLocator()
    blanks = locator.locate(GRID_G1)
    assert blanks == [(2, 2), (3, 3)]


def test_missing_numbers_g1() -> None:
    finder = MissingNumberFinder()
    assert finder.find(GRID_G1) == [1, 6]


def test_validator_complete_magic_constant() -> None:
    grid = [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
    assert MagicSquareValidator().is_valid_complete(grid)
    assert sum(grid[0]) == MAGIC_CONSTANT


def test_solver_g1_reverse_success() -> None:
    solver = TwoCellSolver()
    assert solver.solve(GRID_G1) == G1_EXPECTED


def test_solver_raises_when_no_valid_placement(monkeypatch: pytest.MonkeyPatch) -> None:
    """Force both placement attempts to fail."""
    solver = TwoCellSolver()
    monkeypatch.setattr(
        solver._validator,
        "is_valid_complete",
        lambda _g: False,
    )
    with pytest.raises(UnsolvableDomainError):
        solver.solve(GRID_G1)
