# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PartialPreviewResponse", "Error"]


class Error(BaseModel):
    message: str
    """A human-readable description of the error."""

    field: Optional[str] = None
    """The partial field that caused the error, if available."""


class PartialPreviewResponse(BaseModel):
    """A response to a partial preview request."""

    result: Literal["success", "error"]
    """The result of the preview."""

    type: Literal["html", "text", "json", "markdown"]
    """The partial type that was rendered."""

    content: Optional[str] = None
    """The rendered partial content. Present when result is `success`."""

    errors: Optional[List[Error]] = None
    """A list of errors encountered during rendering. Present when result is `error`."""
