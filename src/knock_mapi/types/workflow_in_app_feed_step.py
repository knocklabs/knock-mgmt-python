# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .send_window import SendWindow
from .condition_group import ConditionGroup
from .in_app_feed_template import InAppFeedTemplate
from .in_app_feed_channel_settings import InAppFeedChannelSettings

__all__ = ["WorkflowInAppFeedStep"]


class WorkflowInAppFeedStep(BaseModel):
    """An in-app feed step within a workflow.

    Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    template: InAppFeedTemplate
    """An in-app feed template."""

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

    channel_overrides: Optional[InAppFeedChannelSettings] = None
    """In-app feed channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Optional[Literal["in_app_feed"]] = None
    """The type of the channel step. Always `in_app_feed` for in-app feed steps."""

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
