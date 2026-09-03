# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .goal_condition import GoalCondition

__all__ = ["Goal"]


class Goal(BaseModel):
    """
    A goal defines an event condition that is tracked and attributed to messaging resources.
    """

    condition: GoalCondition
    """
    A goal condition consisting of a polymorphic event and optional match
    conditions.
    """

    created_at: datetime
    """The timestamp of when the goal was created. (read-only)."""

    environment: str
    """The slug of the environment in which the goal exists. (read-only)."""

    key: str
    """The unique key string for the goal.

    Must be at minimum 1 character and at maximum 255 characters in length.
    """

    name: str
    """A name for the goal.

    Must be at minimum 1 character and at maximum 255 characters in length.
    """

    sha: str
    """The SHA hash of the goal data. (read-only)."""

    updated_at: datetime
    """The timestamp of when the goal was last updated. (read-only)."""

    description: Optional[str] = None
    """An optional description for the goal. Maximum of 280 characters allowed."""
