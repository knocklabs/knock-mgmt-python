# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .send_window import SendWindow
from .sms_template import SMSTemplate
from .condition_group import ConditionGroup
from .sms_channel_settings import SMSChannelSettings

__all__ = ["WorkflowSMSStep"]


class WorkflowSMSStep(BaseModel):
    """A SMS step within a workflow.

    Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    template: SMSTemplate
    """An SMS template."""

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

    channel_overrides: Optional[SMSChannelSettings] = None
    """SMS channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Optional[Literal["sms"]] = None
    """The type of the channel step. Always `sms` for SMS steps."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""

    send_windows: Optional[List[SendWindow]] = None
    """A list of send window objects.

    Must include one send window object per day of the week.
    """
