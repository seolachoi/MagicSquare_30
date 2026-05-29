"""Shared pytest fixtures."""

import pytest

# G1: reverse-success grid (workbook SC-DOM-SOL-001)
GRID_G1 = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]

G1_EXPECTED = [3, 3, 6, 4, 4, 1]


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """Partial grid where small-first fails, reverse succeeds."""
    return [row[:] for row in GRID_G1]
