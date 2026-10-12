# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ReusableRequestArchiveResponse"]


class ReusableRequestArchiveResponse(BaseModel):
    """The response from archiving a reusable request."""

    result: str
    """The result of the archive operation."""
