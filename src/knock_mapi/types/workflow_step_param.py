# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from .._compat import PYDANTIC_V1
from .send_window_param import SendWindowParam
from .sms_template_param import SMSTemplateParam
from .chat_template_param import ChatTemplateParam
from .push_template_param import PushTemplateParam
from .email_template_param import EmailTemplateParam
from .condition_group_param import ConditionGroupParam
from .webhook_template_param import WebhookTemplateParam
from .workflow_batch_step_param import WorkflowBatchStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam
from .workflow_fetch_step_param import WorkflowFetchStepParam
from .in_app_feed_template_param import InAppFeedTemplateParam
from .sms_channel_settings_param import SMSChannelSettingsParam
from .chat_channel_settings_param import ChatChannelSettingsParam
from .push_channel_settings_param import PushChannelSettingsParam
from .email_channel_settings_param import EmailChannelSettingsParam
from .workflow_throttle_step_param import WorkflowThrottleStepParam
from .in_app_feed_channel_settings_param import InAppFeedChannelSettingsParam
from .workflow_trigger_workflow_step_param import WorkflowTriggerWorkflowStepParam

__all__ = [
    "WorkflowStepParam",
    "WorkflowWebhookStep",
    "WorkflowInAppFeedStep",
    "WorkflowChatStep",
    "WorkflowSMSStep",
    "WorkflowPushStep",
    "WorkflowEmailStep",
]


class WorkflowWebhookStep(TypedDict, total=False):
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

    channel_type: Literal["http"]
    """The type of the channel step. Always `http` for webhook steps."""

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


class WorkflowInAppFeedStep(TypedDict, total=False):
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


class WorkflowChatStep(TypedDict, total=False):
    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[ChatTemplateParam]
    """A chat template."""

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


class WorkflowSMSStep(TypedDict, total=False):
    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[SMSTemplateParam]
    """An SMS template."""

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

    channel_overrides: Optional[SMSChannelSettingsParam]
    """SMS channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Literal["sms"]
    """The type of the channel step. Always `sms` for SMS steps."""

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


class WorkflowPushStep(TypedDict, total=False):
    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[PushTemplateParam]
    """A push notification template."""

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

    channel_overrides: Optional[PushChannelSettingsParam]
    """Push channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Literal["push"]
    """The type of the channel step. Always `push` for push steps."""

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


class WorkflowEmailStep(TypedDict, total=False):
    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    template: Required[EmailTemplateParam]
    """An email message template."""

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

    channel_overrides: Optional[EmailChannelSettingsParam]
    """Email channel settings.

    Only used as configuration as part of a workflow channel step.
    """

    channel_type: Literal["email"]
    """The type of the channel step. Always `email` for email steps."""

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


if TYPE_CHECKING or not PYDANTIC_V1:
    WorkflowStepParam = TypeAliasType(
        "WorkflowStepParam",
        Union[
            WorkflowWebhookStep,
            WorkflowInAppFeedStep,
            WorkflowChatStep,
            WorkflowSMSStep,
            WorkflowPushStep,
            WorkflowEmailStep,
            WorkflowDelayStepParam,
            WorkflowBatchStepParam,
            WorkflowFetchStepParam,
            WorkflowThrottleStepParam,
            "WorkflowBranchStepParam",
            WorkflowTriggerWorkflowStepParam,
        ],
    )
else:
    WorkflowStepParam: TypeAlias = Union[
        WorkflowWebhookStep,
        WorkflowInAppFeedStep,
        WorkflowChatStep,
        WorkflowSMSStep,
        WorkflowPushStep,
        WorkflowEmailStep,
        WorkflowDelayStepParam,
        WorkflowBatchStepParam,
        WorkflowFetchStepParam,
        WorkflowThrottleStepParam,
        "WorkflowBranchStepParam",
        WorkflowTriggerWorkflowStepParam,
    ]

from .workflow_branch_step_param import WorkflowBranchStepParam
