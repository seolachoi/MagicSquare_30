"""Maps Domain exceptions to Boundary failure envelopes (E006/E007)."""

from __future__ import annotations

from boundary.schemas import ErrorDetail, FailureResponse
from entity.exceptions.domain_errors import UnsolvableDomainError

_E006_CODE = "E006"
_E006_MESSAGE = "UNSOLVABLE: no valid magic square completion"


class ErrorMapper:
    """Translates Domain errors into PRD §12.3 Boundary error codes."""

    def map_domain_error(self, error: Exception) -> FailureResponse:
        """Map a Domain exception to a ``FailureResponse``.

        Args:
            error: Domain-layer exception raised during solve.

        Returns:
            Failure envelope with PRD error code.

        Raises:
            Exception: Re-raises when no mapping is defined (e.g. E007 TBD).
        """
        if isinstance(error, UnsolvableDomainError):
            return FailureResponse(
                type="ERROR",
                error=ErrorDetail(code=_E006_CODE, message=_E006_MESSAGE),
            )
        raise error
