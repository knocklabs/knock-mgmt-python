# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .send_window_param import SendWindowParam
from .condition_group_param import ConditionGroupParam
from .in_app_feed_template_param import InAppFeedTemplateParam
from .in_app_feed_channel_settings_param import InAppFeedChannelSettingsParam

__all__ = ["WorkflowInAppFeedStepParam"]


class WorkflowInAppFeedStepParam(TypedDict, total=False):
    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[InAppFeedTemplateParam]
    """An in-app feed template."""

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

    channel_overrides: Optional[InAppFeedChannelSettingsParam]
    """In-app feed channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Literal["in_app_feed"]
    """The type of the channel step. Always `in_app_feed` for in-app feed steps."""

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
