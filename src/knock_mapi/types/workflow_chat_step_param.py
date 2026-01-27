# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .send_window_param import SendWindowParam
from .chat_template_param import ChatTemplateParam
from .condition_group_param import ConditionGroupParam
from .chat_channel_settings_param import ChatChannelSettingsParam

__all__ = ["WorkflowChatStepParam"]


class WorkflowChatStepParam(TypedDict, total=False):
    """A chat step within a workflow.

    Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[ChatTemplateParam]
    """A chat template."""

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

    channel_overrides: Optional[ChatChannelSettingsParam]
    """Chat channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Literal["chat"]
    """The type of the channel step. Always `chat` for chat steps."""

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
