# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .send_window_param import SendWindowParam
from .sms_template_param import SMSTemplateParam
from .condition_group_param import ConditionGroupParam
from .sms_channel_settings_param import SMSChannelSettingsParam

__all__ = ["WorkflowSMSStepParam"]


class WorkflowSMSStepParam(TypedDict, total=False):
    """A SMS step within a workflow.

    Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[SMSTemplateParam]
    """An SMS template."""

    type: Required[Literal["channel"]]
    """The type of the workflow step."""

    channel_group_key: Optional[str]
    """
    The key of the channel group to which the channel step will be sending a
    notification. A channel step can have either a channel key or a channel group
    key, but not both.
    """

    channel_key: Optional[str]
    """The key of the channel to which the channel step will be sending a notification.

    A channel step can have either a channel key or a channel group key, but not
    both.
    """

    channel_overrides: Optional[SMSChannelSettingsParam]
    """SMS channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Literal["sms"]
    """The type of the channel step. Always `sms` for SMS steps."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""

    send_windows: Optional[Iterable[SendWindowParam]]
    """A list of send window objects.

    Must include one send window object per day of the week.
    """
