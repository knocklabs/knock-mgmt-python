# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .duration_param import DurationParam
from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowThrottleStepParam", "Settings"]


class Settings(TypedDict, total=False):
    throttle_key: Optional[str]
    """The data property to use to throttle notifications per recipient."""

    throttle_limit: Optional[int]
    """The maximum number of workflows to allow within the duration window.

    Defaults to 1.
    """

    throttle_window: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    throttle_window_field_path: Optional[str]
    """The data path to resolve a dynamic throttle window.

    The resolved value must be an ISO-8601 timestamp. See more in the
    [docs](https://docs.knock.app/designing-workflows/throttle-function#set-a-dynamic-throttle-window).
    """


class WorkflowThrottleStepParam(TypedDict, total=False):
    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[Settings]
    """The settings for the throttle step."""

    type: Required[Literal["throttle"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""
