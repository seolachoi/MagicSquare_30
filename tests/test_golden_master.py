"""Golden master regression — G1 success path."""

import pytest

from boundary.ui_boundary import UIBoundary
from tests.conftest import G1_EXPECTED, GRID_G1

EXPECTED_SNAPSHOT = "G1_OK=" + ",".join(str(x) for x in G1_EXPECTED)


@pytest.mark.golden_master
def test_g1_golden_master_output() -> None:
    result = UIBoundary().solve(GRID_G1)
    assert result.type == "OK"
    actual = "G1_OK=" + ",".join(str(x) for x in result.data)
    assert actual == EXPECTED_SNAPSHOT
