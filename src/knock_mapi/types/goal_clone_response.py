# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .goal import Goal
from .._models import BaseModel

__all__ = ["GoalCloneResponse"]


class GoalCloneResponse(BaseModel):
    """Wraps the Goal response under the `goal` key."""

    goal: Goal
    """
    A goal defines an event condition that is tracked and attributed to messaging
    resources.
    """
