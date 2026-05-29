"""Boundary Screen — MagicSquareMainWindow UI contract tests."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

pytest.importorskip("PyQt6")

from PyQt6.QtWidgets import QApplication

from boundary.schemas import FailureResponse, SuccessResponse
from boundary.screen.main_window import G1_DEFAULT_GRID, MagicSquareMainWindow
from boundary.ui_boundary import UIBoundary
from control.solve_partial_magic_square import SolvePartialMagicSquare

from tests.conftest import G1_EXPECTED, GRID_G0


@pytest.fixture(scope="module")
def qt_app() -> QApplication:
    """Shared QApplication for headless widget tests."""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture
def real_boundary() -> UIBoundary:
    """Real UIBoundary stack wired like ``boundary.screen.app``."""
    return UIBoundary(solve_use_case=SolvePartialMagicSquare())


class TestMagicSquareMainWindowLayout:
    """Screen layout and default fixture contract."""

    def test_window_title_and_spinbox_grid(
        self, qt_app: QApplication, real_boundary: UIBoundary
    ) -> None:
        window = MagicSquareMainWindow(real_boundary)
        assert window.windowTitle() == "Magic Square 4x4"
        assert len(window._spinboxes) == 4
        assert all(len(row) == 4 for row in window._spinboxes)

    def test_default_grid_matches_g1_fixture(
        self, qt_app: QApplication, real_boundary: UIBoundary
    ) -> None:
        window = MagicSquareMainWindow(real_boundary)
        assert window._read_grid() == G1_DEFAULT_GRID


class TestMagicSquareMainWindowSolve:
    """Solve action renders Boundary DTO results in the result label."""

    def test_g1_solve_shows_success_message(
        self, qt_app: QApplication, real_boundary: UIBoundary
    ) -> None:
        window = MagicSquareMainWindow(real_boundary)
        window._on_solve()
        text = window._result_label.text()
        assert text.startswith("결과 (r1, c1, n1, r2, c2, n2):")
        for value in G1_EXPECTED:
            assert str(value) in text

    def test_complete_grid_shows_validation_error(
        self, qt_app: QApplication, real_boundary: UIBoundary
    ) -> None:
        window = MagicSquareMainWindow(real_boundary)
        for row_index, row_boxes in enumerate(window._spinboxes):
            for col_index, spinbox in enumerate(row_boxes):
                spinbox.setValue(GRID_G0[row_index][col_index])
        window._on_solve()
        assert window._result_label.text().startswith("오류:")
        assert "INVALID_EMPTY_COUNT" in window._result_label.text()

    def test_mock_boundary_failure_message(self, qt_app: QApplication) -> None:
        from boundary.schemas import ErrorDetail

        mock_boundary = MagicMock(spec=UIBoundary)
        mock_boundary.solve.return_value = FailureResponse(
            type="ERROR",
            error=ErrorDetail(
                code="E006",
                message="UNSOLVABLE: no valid magic square completion",
            ),
        )
        window = MagicSquareMainWindow(mock_boundary)
        window._on_solve()
        assert "UNSOLVABLE" in window._result_label.text()

    def test_mock_boundary_success_message(
        self, qt_app: QApplication
    ) -> None:
        mock_boundary = MagicMock(spec=UIBoundary)
        mock_boundary.solve.return_value = SuccessResponse(
            type="OK", data=[1, 2, 3, 4, 5, 6]
        )
        window = MagicSquareMainWindow(mock_boundary)
        window._on_solve()
        assert "1, 2, 3, 4, 5, 6" in window._result_label.text()
