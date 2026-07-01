# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AudienceArchiveResponse"]


class AudienceArchiveResponse(BaseModel):
    """The response from archiving an audience."""

    result: str
    """The result of the archive operation."""
