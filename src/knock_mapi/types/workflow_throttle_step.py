# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .duration import Duration
from .condition_group import ConditionGroup

__all__ = ["WorkflowThrottleStep", "Settings"]


class Settings(BaseModel):
    """The settings for the throttle step."""

    throttle_key: Optional[str] = None
    """The data property to use to throttle notifications per recipient."""

    throttle_limit: Optional[int] = None
    """The maximum number of workflows to allow within the duration window.

    Defaults to 1.
    """

    throttle_window: Optional[Duration] = None
    """A duration of time, represented as a unit and a value."""

    throttle_window_field_path: Optional[str] = None
    """The data path to resolve a dynamic throttle window.

    The resolved value must be an ISO-8601 timestamp. See more in the
    [docs](https://docs.knock.app/designing-workflows/throttle-function#set-a-dynamic-throttle-window).
    """


class WorkflowThrottleStep(BaseModel):
    """A throttle function step.

    Read more in the [docs](https://docs.knock.app/designing-workflows/throttle-function).
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Settings
    """The settings for the throttle step."""

    type: Literal["throttle"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""
