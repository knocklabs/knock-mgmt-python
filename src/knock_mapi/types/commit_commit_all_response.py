# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CommitCommitAllResponse"]


class CommitCommitAllResponse(BaseModel):
    result: str
    """The result of the commit operation."""
