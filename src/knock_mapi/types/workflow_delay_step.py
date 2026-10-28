# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .duration import Duration
from .condition_group import ConditionGroup

__all__ = ["WorkflowDelayStep", "Settings", "SettingsDelayUntilTimeWindow"]


class SettingsDelayUntilTimeWindow(BaseModel):
    """A time window for a delay step.

    Describes a single day and when the delay can resume on it.
    """

    day: Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    """The day of the week."""

    type: Literal["open", "closed"]
    """Whether the delay can resume on this day.

    A `closed` day does not support `from` and `until`.
    """

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The time the window opens. When blank, the window is open all day."""

    until: Optional[str] = None
    """The time the window closes.

    When blank, the window is open until the end of the day.
    """


class Settings(BaseModel):
    """The settings for the delay step.

    Set `delay_for` for a fixed delay, `delay_until_field_path` for a dynamic delay, both for a relative delay, or `delay_until_time_windows` to wait until a weekly schedule is open.
    """

    delay_for: Optional[Duration] = None
    """A duration of time, represented as a unit and a value."""

    delay_until_field_path: Optional[str] = None
    """
    When set will use the path to resolve the delay into a timestamp from the
    property referenced. The resolved timestamp must be 365 days or less from when
    the step runs.
    """

    delay_until_time_windows: Optional[List[SettingsDelayUntilTimeWindow]] = None
    """A weekly schedule of when the delay can resume.

    Must include one window per day, and at least one day must be open. Cannot be
    combined with `delay_for` or `delay_until_field_path`.
    """

    workflow_version_mode: Optional[Literal["pinned", "latest"]] = None
    """
    Whether the delay is pinned to the opening workflow version or continues on the
    latest compatible version when the delay elapses. One of: `pinned` or `latest`.
    New delay steps default to `latest`. Configs that omit the field hydrate as
    `pinned`.
    """


class WorkflowDelayStep(BaseModel):
    """A delay function step.

    Read more in the [docs](https://docs.knock.app/designing-workflows/delay-function).
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Settings
    """The settings for the delay step.

    Set `delay_for` for a fixed delay, `delay_until_field_path` for a dynamic delay,
    both for a relative delay, or `delay_until_time_windows` to wait until a weekly
    schedule is open.
    """

    type: Literal["delay"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""
