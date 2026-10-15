# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .duration_param import DurationParam
from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowDelayStepParam", "Settings", "SettingsDelayUntilTimeWindow"]

_SettingsDelayUntilTimeWindowReservedKeywords = TypedDict(
    "_SettingsDelayUntilTimeWindowReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class SettingsDelayUntilTimeWindow(_SettingsDelayUntilTimeWindowReservedKeywords, total=False):
    """A time window for a delay step.

    Describes a single day and when the delay can resume on it.
    """

    day: Required[Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]]
    """The day of the week."""

    type: Required[Literal["open", "closed"]]
    """Whether the delay can resume on this day.

    A `closed` day does not support `from` and `until`.
    """

    until: Optional[str]
    """The time the window closes.

    When blank, the window is open until the end of the day.
    """


class Settings(TypedDict, total=False):
    """The settings for the delay step.

    Set `delay_for` for a fixed delay, `delay_until_field_path` for a dynamic delay, both for a relative delay, or `delay_until_time_windows` to wait until a weekly schedule is open.
    """

    delay_for: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    delay_until_field_path: str
    """
    When set will use the path to resolve the delay into a timestamp from the
    property referenced
    """

    delay_until_time_windows: Optional[Iterable[SettingsDelayUntilTimeWindow]]
    """A weekly schedule of when the delay can resume.

    Must include one window per day, and at least one day must be open. Cannot be
    combined with `delay_for` or `delay_until_field_path`.
    """

    workflow_version_mode: Optional[Literal["pinned", "latest"]]
    """
    Whether the delay is pinned to the opening workflow version or continues on the
    latest compatible version when the delay elapses. One of: `pinned` or `latest`.
    New delay steps default to `latest`. Configs that omit the field hydrate as
    `pinned`.
    """


class WorkflowDelayStepParam(TypedDict, total=False):
    """A delay function step.

    Read more in the [docs](https://docs.knock.app/designing-workflows/delay-function).
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[Settings]
    """The settings for the delay step.

    Set `delay_for` for a fixed delay, `delay_until_field_path` for a dynamic delay,
    both for a relative delay, or `delay_until_time_windows` to wait until a weekly
    schedule is open.
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
