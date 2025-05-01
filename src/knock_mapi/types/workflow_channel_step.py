# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .send_window import SendWindow
from .sms_template import SMSTemplate
from .chat_template import ChatTemplate
from .push_template import PushTemplate
from .email_template import EmailTemplate
from .condition_group import ConditionGroup
from .webhook_template import WebhookTemplate
from .in_app_feed_template import InAppFeedTemplate
from .sms_channel_settings import SMSChannelSettings
from .chat_channel_settings import ChatChannelSettings
from .push_channel_settings import PushChannelSettings
from .email_channel_settings import EmailChannelSettings
from .in_app_feed_channel_settings import InAppFeedChannelSettings

__all__ = ["WorkflowChannelStep", "Template", "ChannelOverrides"]

Template: TypeAlias = Union[EmailTemplate, InAppFeedTemplate, SMSTemplate, PushTemplate, ChatTemplate, WebhookTemplate]

ChannelOverrides: TypeAlias = Union[
    EmailChannelSettings, InAppFeedChannelSettings, SMSChannelSettings, PushChannelSettings, ChatChannelSettings, None
]


class WorkflowChannelStep(BaseModel):
    name: str
    """A name for the workflow step."""

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Template
    """The message template for the channel step.

    The shape of the template depends on the type of the channel you'll be sending
    to. See below for definitions of each channel type template: email, in-app, SMS,
    push, chat, and webhook.
    """

    type: Literal["channel"]
    """The type of the workflow step."""

    channel_group_key: Optional[str] = None
    """
    The key of the channel group to which the channel step will be sending a
    notification. A channel step can have either a channel key or a channel group
    key, but not both.
    """

    channel_key: Optional[str] = None
    """The key of the channel to which the channel step will be sending a notification.

    A channel step can have either a channel key or a channel group key, but not
    both.
    """

    channel_overrides: Optional[ChannelOverrides] = None
    """A map of channel overrides for the channel step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    send_windows: Optional[List[SendWindow]] = None
    """A list of send window objects.

    Must include one send window object per day of the week.
    """
