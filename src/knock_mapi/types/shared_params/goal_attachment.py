# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GoalAttachment"]


class GoalAttachment(TypedDict, total=False):
    """
    Deprecated: attach goals with `PUT /v1/goals/{goal_key}/attachments/{resource_type}/{resource_key}` instead. Attaches a goal to a workflow, guide, or broadcast for attribution tracking. For accounts on the new goal attachments, saves that include this field are rejected with a 422 and responses omit it.
    """

    goal_key: Required[str]
    """The key of the goal to attach."""

    attribution_window_days: int
    """The number of days to attribute conversions after the notification is sent.

    Must be between 1 and 30. Defaults to 7.
    """
