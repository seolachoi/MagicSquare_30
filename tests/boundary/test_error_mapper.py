"""ErrorMapper — Domain exception to Boundary envelope mapping."""

from __future__ import annotations

from boundary.error_mapper import ErrorMapper
from entity.exceptions.domain_errors import UnsolvableDomainError


def test_map_unsolvable_domain_error_to_e006() -> None:
    mapper = ErrorMapper()
    result = mapper.map_domain_error(UnsolvableDomainError("No valid completion"))
    assert result.type == "ERROR"
    assert result.error.code == "E006"
    assert result.error.message == "UNSOLVABLE: no valid magic square completion"
