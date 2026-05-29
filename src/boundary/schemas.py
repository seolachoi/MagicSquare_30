"""Boundary response schemas."""

from typing import List, Literal, Union

from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    """Structured error payload."""

    code: str
    message: str


class FailureResponse(BaseModel):
    """Validation or solve failure envelope."""

    type: Literal["ERROR"] = "ERROR"
    error: ErrorDetail


class SuccessResponse(BaseModel):
    """Successful solve envelope."""

    type: Literal["OK"] = "OK"
    data: List[int] = Field(..., min_length=6, max_length=6)


BoundaryResponse = Union[FailureResponse, SuccessResponse]
