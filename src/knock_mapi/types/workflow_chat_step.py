# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .send_window import SendWindow
from .chat_template import ChatTemplate
from .condition_group import ConditionGroup
from .chat_channel_settings import ChatChannelSettings

__all__ = ["WorkflowChatStep"]


class WorkflowChatStep(BaseModel):
    name: str
    """A name for the workflow step."""

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    template: ChatTemplate
    """A chat template."""

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

    channel_overrides: Optional[ChatChannelSettings] = None
    """Chat channel settings.

    Only used as configuration as part of a workflow channel step.
    """

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
