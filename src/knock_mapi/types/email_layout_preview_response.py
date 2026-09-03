# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmailLayoutPreviewResponse", "Error", "Layout"]


class Error(BaseModel):
    """A rendering error with optional location information."""

    message: str
    """A human-readable description of the error."""

    field: Optional[str] = None
    """The layout field that caused the error, if available."""

    line: Optional[int] = None
    """The line number where the error occurred, if available."""


class Layout(BaseModel):
    """The rendered email layout, ready to be previewed."""

    html_body: Optional[str] = None
    """The fully rendered HTML body of the email layout."""

    text_body: Optional[str] = None
    """The fully rendered plain text body of the email layout."""


class EmailLayoutPreviewResponse(BaseModel):
    """A response to an email layout preview request."""

    result: Literal["success", "error"]
    """The result of the preview."""

    errors: Optional[List[Error]] = None
    """A list of errors encountered during rendering. Present when result is "error"."""

    layout: Optional[Layout] = None
    """The rendered email layout, ready to be previewed."""
