"""Shared pytest configuration and fixtures."""

import sys
from pathlib import Path

import pytest

SRC_PATH = Path(__file__).resolve().parent.parent / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

pytest_plugins = ["tests.golden_master_conftest"]

# Report/02 G0~G3 grid SSOT (Report/05 §9 G2 공식 확정)
GRID_G0 = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]
GRID_G1 = [[16, 3, 2, 13], [5, 0, 11, 8], [9, 6, 0, 12], [4, 15, 14, 1]]
GRID_G2 = [[16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 0, 12], [4, 14, 15, 0]]
GRID_G3 = [[1, 2, 3, 0], [5, 6, 0, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

G1_EXPECTED = [2, 2, 10, 3, 3, 7]
G2_EXPECTED = [3, 3, 6, 4, 4, 1]


@pytest.fixture
def grid_g0() -> list[list[int]]:
    return [row[:] for row in GRID_G0]


@pytest.fixture
def grid_g1() -> list[list[int]]:
    return [row[:] for row in GRID_G1]


@pytest.fixture
def grid_g2() -> list[list[int]]:
    return [row[:] for row in GRID_G2]


@pytest.fixture
def grid_g3() -> list[list[int]]:
    return [row[:] for row in GRID_G3]
