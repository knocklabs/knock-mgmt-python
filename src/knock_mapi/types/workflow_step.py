# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .send_window import SendWindow
from .sms_template import SMSTemplate
from .chat_template import ChatTemplate
from .push_template import PushTemplate
from .email_template import EmailTemplate
from .condition_group import ConditionGroup
from .webhook_template import WebhookTemplate
from .workflow_batch_step import WorkflowBatchStep
from .workflow_delay_step import WorkflowDelayStep
from .workflow_fetch_step import WorkflowFetchStep
from .in_app_feed_template import InAppFeedTemplate
from .sms_channel_settings import SMSChannelSettings
from .chat_channel_settings import ChatChannelSettings
from .push_channel_settings import PushChannelSettings
from .email_channel_settings import EmailChannelSettings
from .workflow_throttle_step import WorkflowThrottleStep
from .in_app_feed_channel_settings import InAppFeedChannelSettings
from .workflow_trigger_workflow_step import WorkflowTriggerWorkflowStep

__all__ = [
    "WorkflowStep",
    "WorkflowWebhookStep",
    "WorkflowInAppFeedStep",
    "WorkflowChatStep",
    "WorkflowSMSStep",
    "WorkflowPushStep",
    "WorkflowEmailStep",
]


class WorkflowWebhookStep(BaseModel):
    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    template: WebhookTemplate
    """A webhook template.

    By default, a webhook step will use the request settings you configured in your
    webhook channel. You can override this as you see fit on a per-step basis.
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

    channel_type: Optional[Literal["http"]] = None
    """The type of the channel step. Always `http` for webhook steps."""

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


class WorkflowInAppFeedStep(BaseModel):
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


class WorkflowChatStep(BaseModel):
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

    channel_type: Optional[Literal["chat"]] = None
    """The type of the channel step. Always `chat` for chat steps."""

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


class WorkflowSMSStep(BaseModel):
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


class WorkflowPushStep(BaseModel):
    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    template: PushTemplate
    """A push notification template."""

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

    channel_overrides: Optional[PushChannelSettings] = None
    """Push channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Optional[Literal["push"]] = None
    """The type of the channel step. Always `push` for push steps."""

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


class WorkflowEmailStep(BaseModel):
    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    template: EmailTemplate
    """An email message template."""

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

    channel_overrides: Optional[EmailChannelSettings] = None
    """Email channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Optional[Literal["email"]] = None
    """The type of the channel step. Always `email` for email steps."""

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


if TYPE_CHECKING or not PYDANTIC_V1:
    WorkflowStep = TypeAliasType(
        "WorkflowStep",
        Union[
            WorkflowWebhookStep,
            WorkflowInAppFeedStep,
            WorkflowChatStep,
            WorkflowSMSStep,
            WorkflowPushStep,
            WorkflowEmailStep,
            WorkflowDelayStep,
            WorkflowBatchStep,
            WorkflowFetchStep,
            WorkflowThrottleStep,
            "WorkflowBranchStep",
            WorkflowTriggerWorkflowStep,
        ],
    )
else:
    WorkflowStep: TypeAlias = Union[
        WorkflowWebhookStep,
        WorkflowInAppFeedStep,
        WorkflowChatStep,
        WorkflowSMSStep,
        WorkflowPushStep,
        WorkflowEmailStep,
        WorkflowDelayStep,
        WorkflowBatchStep,
        WorkflowFetchStep,
        WorkflowThrottleStep,
        "WorkflowBranchStep",
        WorkflowTriggerWorkflowStep,
    ]

from .workflow_branch_step import WorkflowBranchStep
