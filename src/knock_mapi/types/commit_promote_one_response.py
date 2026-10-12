# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .commit import Commit
from .._models import BaseModel
from .promote_group import PromoteGroup

__all__ = ["CommitPromoteOneResponse"]


class CommitPromoteOneResponse(BaseModel):
    """Wraps the Commit response under the `commit` key."""

    commit: Commit
    """A commit is a change to a resource within an environment, made by an author."""

    promote_group: PromoteGroup
    """A summary of a promote.

    Every commit copied into the destination environment by the same promote shares
    the group's ID, which you can use to list them with the `promote_group_id`
    filter on the list commits endpoint.
    """
