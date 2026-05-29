"""Boundary input validation tests — Track A."""

import pytest

from boundary.input_validator import InputValidator


@pytest.fixture
def validator() -> InputValidator:
    return InputValidator()


def test_none_returns_e003(validator: InputValidator) -> None:
    # AC: null grid
    result = validator.validate(None)
    assert result is not None
    assert result.error.code == "E003"


def test_not_4x4_returns_e001(validator: InputValidator) -> None:
    result = validator.validate([[1, 2], [3, 4]])
    assert result is not None
    assert result.error.code == "E001"


def test_one_blank_returns_e002(validator: InputValidator) -> None:
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    result = validator.validate(grid)
    assert result is not None
    assert result.error.code == "E002"


def test_value_17_returns_e004(validator: InputValidator) -> None:
    grid = [[17, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    result = validator.validate(grid)
    assert result is not None
    assert result.error.code == "E004"


def test_duplicate_returns_e005(validator: InputValidator) -> None:
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 15]]
    result = validator.validate(grid)
    assert result is not None
    assert result.error.code == "E005"


def test_valid_g1_returns_none(validator: InputValidator, grid_g1: list[list[int]]) -> None:
    assert validator.validate(grid_g1) is None
