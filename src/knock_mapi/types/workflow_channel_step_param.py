# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .send_window_param import SendWindowParam
from .sms_template_param import SMSTemplateParam
from .chat_template_param import ChatTemplateParam
from .push_template_param import PushTemplateParam
from .email_template_param import EmailTemplateParam
from .condition_group_param import ConditionGroupParam
from .webhook_template_param import WebhookTemplateParam
from .in_app_feed_template_param import InAppFeedTemplateParam
from .sms_channel_settings_param import SMSChannelSettingsParam
from .chat_channel_settings_param import ChatChannelSettingsParam
from .push_channel_settings_param import PushChannelSettingsParam
from .email_channel_settings_param import EmailChannelSettingsParam
from .in_app_feed_channel_settings_param import InAppFeedChannelSettingsParam

__all__ = ["WorkflowChannelStepParam", "Template", "ChannelOverrides"]

Template: TypeAlias = Union[
    EmailTemplateParam,
    InAppFeedTemplateParam,
    SMSTemplateParam,
    PushTemplateParam,
    ChatTemplateParam,
    WebhookTemplateParam,
]

ChannelOverrides: TypeAlias = Union[
    EmailChannelSettingsParam,
    InAppFeedChannelSettingsParam,
    SMSChannelSettingsParam,
    PushChannelSettingsParam,
    ChatChannelSettingsParam,
]


class WorkflowChannelStepParam(TypedDict, total=False):
    name: Required[str]
    """A name for the workflow step."""

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[Template]
    """The message template for the channel step.

    The shape of the template depends on the type of the channel you'll be sending
    to. See below for definitions of each channel type template: email, in-app, SMS,
    push, chat, and webhook.
    """

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

    channel_overrides: Optional[ChannelOverrides]
    """A map of channel overrides for the channel step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    send_windows: Optional[Iterable[SendWindowParam]]
    """A list of send window objects.

    Must include one send window object per day of the week.
    """
