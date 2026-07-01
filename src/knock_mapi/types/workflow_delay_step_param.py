# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .duration_param import DurationParam
from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowDelayStepParam", "Settings"]


class Settings(TypedDict, total=False):
    """The settings for the delay step.

    Both fields can be set to compute a delay where `delay_for` is an offset from the `delay_until_field_path`.
    """

    delay_for: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    delay_until_field_path: str
    """
    When set will use the path to resolve the delay into a timestamp from the
    property referenced
    """


class WorkflowDelayStepParam(TypedDict, total=False):
    """A delay function step.

    Read more in the [docs](https://docs.knock.app/designing-workflows/delay-function).
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[Settings]
    """The settings for the delay step.

    Both fields can be set to compute a delay where `delay_for` is an offset from
    the `delay_until_field_path`.
    """

    type: Required[Literal["delay"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""
