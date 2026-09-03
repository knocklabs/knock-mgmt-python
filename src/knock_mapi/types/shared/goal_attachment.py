# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GoalAttachment"]


class GoalAttachment(BaseModel):
    """Attaches a goal to a workflow, guide, or broadcast for attribution tracking."""

    goal_key: str
    """The key of the goal to attach."""

    attribution_window_days: Optional[int] = None
    """The number of days to attribute conversions after the notification is sent.

    Must be between 1 and 30. Defaults to 7.
    """
