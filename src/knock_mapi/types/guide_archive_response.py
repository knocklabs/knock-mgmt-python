# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GuideArchiveResponse"]


class GuideArchiveResponse(BaseModel):
    """The response from archiving a guide."""

    result: str
    """The result of the promote operation."""
