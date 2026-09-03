# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .send_window_param import SendWindowParam
from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowInAppGuideStepParam"]


class WorkflowInAppGuideStepParam(TypedDict, total=False):
    """An in-app guide step within a workflow.

    References a guide that will be shown to recipients who execute this step. Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).
    """

    channel_type: Required[Literal["in_app_guide"]]
    """The type of the channel step. Always `in_app_guide` for in-app guide steps."""

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

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

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    guide_key: Optional[str]
    """The key of the guide to reference.

    When a recipient executes this step they are added to the managed audience that
    backs the guide's workflow-derived targeting.
    """

    name: Optional[str]
    """A name for the workflow step."""

    send_windows: Optional[Iterable[SendWindowParam]]
    """A list of send window objects.

    Must include one send window object per day of the week.
    """
