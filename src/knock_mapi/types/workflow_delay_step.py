# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .duration import Duration
from .condition_group import ConditionGroup

__all__ = ["WorkflowDelayStep", "Settings"]


class Settings(BaseModel):
    delay_for: Optional[Duration] = None
    """A duration of time, represented as a unit and a value."""

    delay_until_field_path: Optional[str] = None
    """
    When set will use the path to resolve the delay into a timestamp from the
    property referenced
    """


class WorkflowDelayStep(BaseModel):
    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: str
    """A name for the workflow step."""

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Settings
    """The settings for the delay step.

    Both fields can be set to compute a delay where `delay_for` is an offset from
    the `delay_until_field_path`.
    """

    type: Literal["delay"]
    """The type of the workflow step."""
