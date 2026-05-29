"""Boundary validation outcome — explicit pass/fail without control-flow exceptions."""

from __future__ import annotations

from dataclasses import dataclass

from boundary.schemas import ErrorDetail, FailureResponse


@dataclass(frozen=True)
class ValidationResult:
    """Result of ``InputValidator.validate`` — error envelope or valid pass.

    Attributes:
        failure: ``FailureResponse`` when validation fails; ``None`` when valid.
    """

    failure: FailureResponse | None = None

    @classmethod
    def ok(cls) -> ValidationResult:
        """Return a successful validation outcome."""
        return cls(failure=None)

    @classmethod
    def from_failure(cls, response: FailureResponse) -> ValidationResult:
        """Wrap a failure envelope as a validation outcome."""
        return cls(failure=response)

    @property
    def is_valid(self) -> bool:
        """True when the grid passed Boundary input validation."""
        return self.failure is None

    @property
    def is_error(self) -> bool:
        """True when validation failed with a failure envelope."""
        return self.failure is not None

    @property
    def type(self) -> str:
        """Failure discriminator — mirrors ``FailureResponse.type`` on error."""
        if self.failure is None:
            raise AttributeError("valid ValidationResult has no type")
        return self.failure.type

    @property
    def error(self) -> ErrorDetail:
        """Nested error detail — mirrors ``FailureResponse.error`` on error."""
        if self.failure is None:
            raise AttributeError("valid ValidationResult has no error")
        return self.failure.error

    def model_dump(self) -> dict[str, object]:
        """Serialize error envelope for contract tests; valid → empty dict."""
        if self.failure is None:
            return {}
        return self.failure.model_dump()
