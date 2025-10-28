# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .send_window_param import SendWindowParam
from .condition_group_param import ConditionGroupParam
from .webhook_template_param import WebhookTemplateParam

__all__ = ["WorkflowWebhookStepParam"]


class WorkflowWebhookStepParam(TypedDict, total=False):
    name: Required[str]
    """A name for the workflow step."""

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[WebhookTemplateParam]
    """A webhook template.

    By default, a webhook step will use the request settings you configured in your
    webhook channel. You can override this as you see fit on a per-step basis.
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
