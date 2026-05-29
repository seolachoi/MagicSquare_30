"""Domain-level errors."""


class UnsolvableDomainError(Exception):
    """No placement satisfies the magic square invariant."""

    def __init__(self, message: str = "No valid magic square placement.") -> None:
        super().__init__(message)
