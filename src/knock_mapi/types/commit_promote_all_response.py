# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .promote_group import PromoteGroup

__all__ = ["CommitPromoteAllResponse"]


class CommitPromoteAllResponse(BaseModel):
    """The response from promoting all changes."""

    promote_group: Optional[PromoteGroup] = None
    """A summary of a promote.

    Every commit copied into the destination environment by the same promote shares
    the group's ID, which you can use to list them with the `promote_group_id`
    filter on the list commits endpoint.
    """

    result: str
    """The result of the promote operation."""
