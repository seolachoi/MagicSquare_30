"""Report/09 Track B — D-SOL-01~04 two cell solver RED skeleton.

Step A/B 해결 및 출력 계약. Domain Mock 금지. AC-FR05-*.
"""

from __future__ import annotations

import pytest

from entity.exceptions.domain_errors import UnsolvableDomainError
from entity.services.two_cell_solver import TwoCellSolver

from tests.conftest import G1_EXPECTED, G2_EXPECTED, GRID_G1, GRID_G2, GRID_G3


class TestTwoCellSolverStepA:
    """D-SOL-01 — G1 Step B fallback (Step A fails for this fixture)."""

    def test_d_sol_01_g1_step_a_returns_solution(self) -> None:
        """D-SOL-01, I8 — G1 Step B solution → [2,2,10,3,3,7]."""
        solver = TwoCellSolver()
        result = solver.solve(GRID_G1)
        assert result.values == G1_EXPECTED


class TestTwoCellSolverStepB:
    """D-SOL-02 — G2 Step B만 성공."""

    def test_d_sol_02_g2_step_b_only_returns_solution(self) -> None:
        """D-SOL-02, I9 — G2 Step B fallback → [3,3,6,4,4,1]."""
        solver = TwoCellSolver()
        result = solver.solve(GRID_G2)
        assert result.values == G2_EXPECTED


class TestTwoCellSolverUnsolvable:
    """D-SOL-03 — G3 무해 → UnsolvableDomainError."""

    def test_d_sol_03_g3_raises_unsolvable(self) -> None:
        """D-SOL-03, I10 — G3 → UnsolvableDomainError."""
        solver = TwoCellSolver()
        with pytest.raises(UnsolvableDomainError):
            solver.solve(GRID_G3)


class TestTwoCellSolverOutputContract:
    """D-SOL-04 — 반환 길이 6·좌표 1-index."""

    def test_d_sol_04_g1_result_length_and_one_index(self) -> None:
        """D-SOL-04, I8 — G1 len==6, 좌표 ∈ [1,4]."""
        solver = TwoCellSolver()
        result = solver.solve(GRID_G1)
        assert len(result.values) == 6
        r1, c1, _, r2, c2, _ = result.values
        for coord in (r1, c1, r2, c2):
            assert 1 <= coord <= 4
