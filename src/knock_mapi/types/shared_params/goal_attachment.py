# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GoalAttachment"]


class GoalAttachment(TypedDict, total=False):
    """Attaches a goal to a workflow, guide, or broadcast for attribution tracking."""

    goal_key: Required[str]
    """The key of the goal to attach."""

    attribution_window_days: int
    """The number of days to attribute conversions after the notification is sent.

    Must be between 1 and 30. Defaults to 7.
    """
