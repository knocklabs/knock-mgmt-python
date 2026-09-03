# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .goal_condition_param import GoalConditionParam

__all__ = ["GoalRequestParam"]


class GoalRequestParam(TypedDict, total=False):
    """A goal payload for upsert or validate."""

    condition: Required[GoalConditionParam]
    """
    A goal condition consisting of a polymorphic event and optional match
    conditions.
    """

    name: Required[str]
    """A name for the goal.

    Must be at minimum 1 character and at maximum 255 characters in length.
    """

    description: Optional[str]
    """An optional description for the goal. Maximum of 280 characters allowed."""
