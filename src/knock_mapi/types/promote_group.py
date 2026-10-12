# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PromoteGroup", "Actor"]


class Actor(BaseModel):
    """The user who performed the promote."""

    email: Optional[str] = None

    name: Optional[str] = None


class PromoteGroup(BaseModel):
    """A summary of a promote.

    Every commit copied into the destination environment by the same promote shares the group's ID, which you can use to list them with the `promote_group_id` filter on the list commits endpoint.
    """

    id: str
    """The unique identifier for the promote group."""

    commit_count: int
    """The number of commits copied into the destination environment."""

    created_at: datetime
    """The timestamp of when the promote happened."""

    source: str
    """The slug of the environment or branch the commits were promoted from."""

    source_type: Literal["environment", "branch"]
    """Whether the source is an environment or a branch."""

    to_environment: str
    """The slug of the environment the commits were promoted to."""

    actor: Optional[Actor] = None
    """The user who performed the promote."""
