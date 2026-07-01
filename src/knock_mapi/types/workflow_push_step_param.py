# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .send_window_param import SendWindowParam
from .push_template_param import PushTemplateParam
from .condition_group_param import ConditionGroupParam
from .push_channel_settings_param import PushChannelSettingsParam

__all__ = ["WorkflowPushStepParam"]


class WorkflowPushStepParam(TypedDict, total=False):
    """A push step within a workflow.

    Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[PushTemplateParam]
    """A push notification template."""

    type: Required[Literal["channel"]]
    """The type of the workflow step."""

    channel_group_key: Optional[str]
    """
    The key of the channel group to which the channel step will be sending a
    notification. Either `channel_key` or `channel_group_key` must be provided, but
    not both.
    """

    channel_key: Optional[str]
    """
    The key of a specific configured channel instance (e.g., 'knock-email',
    'postmark', 'sendgrid-marketing') to send the notification through. Either
    `channel_key` or `channel_group_key` must be provided, but not both.
    """

    channel_overrides: Optional[PushChannelSettingsParam]
    """Push channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Literal["push"]
    """The type of the channel step. Always `push` for push steps."""

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
