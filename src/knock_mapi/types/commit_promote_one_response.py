# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .commit import Commit
from .._models import BaseModel

__all__ = ["CommitPromoteOneResponse"]


class CommitPromoteOneResponse(BaseModel):
    """Wraps the Commit response under the `commit` key."""

    commit: Commit
    """A commit is a change to a resource within an environment, made by an author."""
