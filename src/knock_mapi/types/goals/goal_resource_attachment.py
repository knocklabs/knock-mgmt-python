# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GoalResourceAttachment"]


class GoalResourceAttachment(BaseModel):
    """A goal attached to a workflow, guide, or broadcast in one environment.

    An attachment goes live without a commit.
    """

    attribution_window_days: int
    """
    The number of days after a message is sent in which a goal completion is
    attributed to it.
    """

    goal_key: str
    """The key of the attached goal."""

    resource_key: str
    """The key of the workflow, guide, or broadcast."""

    resource_type: Literal["workflow", "guide", "broadcast"]
    """The type of resource the goal is attached to."""
