# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CommitPromoteAllResponse"]


class CommitPromoteAllResponse(BaseModel):
    """The response from promoting all changes."""

    result: str
    """The result of the promote operation."""
