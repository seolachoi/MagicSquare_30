"""SC-CTL-001~004 — SolvePartialMagicSquare use-case orchestration."""

from __future__ import annotations

import pytest

from control.solve_partial_magic_square import SolvePartialMagicSquare
from entity.exceptions.domain_errors import UnsolvableDomainError

from tests.conftest import G1_EXPECTED, G2_EXPECTED, GRID_G1, GRID_G2, GRID_G3


class TestSolvePartialMagicSquareOrchestration:
    """Control — TwoCellSolver SSOT orchestration."""

    def test_sc_ctl_001_g1_resolve_returns_solver_ssot(self) -> None:
        """SC-CTL-001 — G1 resolve() → TwoCellSolver Step B placement."""
        use_case = SolvePartialMagicSquare()
        assert use_case.resolve(GRID_G1) == G1_EXPECTED

    def test_sc_ctl_002_g2_resolve_returns_solver_ssot(self) -> None:
        """SC-CTL-002 — G2 resolve() → TwoCellSolver Step B placement."""
        use_case = SolvePartialMagicSquare()
        assert use_case.resolve(GRID_G2) == G2_EXPECTED

    def test_sc_ctl_003_g3_propagates_unsolvable_domain_error(self) -> None:
        """SC-CTL-003 — G3 resolve() propagates UnsolvableDomainError."""
        use_case = SolvePartialMagicSquare()
        with pytest.raises(UnsolvableDomainError):
            use_case.resolve(GRID_G3)

    def test_sc_ctl_004_resolve_matches_direct_solver(self) -> None:
        """SC-CTL-004 — resolve() equals TwoCellSolver.solve().values (SSOT)."""
        from entity.services.two_cell_solver import TwoCellSolver

        use_case = SolvePartialMagicSquare()
        solver = TwoCellSolver()
        for grid in (GRID_G1, GRID_G2):
            assert use_case.resolve(grid) == solver.solve(grid).values
