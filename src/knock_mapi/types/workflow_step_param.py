# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from .._compat import PYDANTIC_V1
from .send_window_param import SendWindowParam
from .condition_group_param import ConditionGroupParam
from .workflow_sms_step_param import WorkflowSMSStepParam
from .workflow_chat_step_param import WorkflowChatStepParam
from .workflow_push_step_param import WorkflowPushStepParam
from .workflow_batch_step_param import WorkflowBatchStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam
from .workflow_email_step_param import WorkflowEmailStepParam
from .workflow_fetch_step_param import WorkflowFetchStepParam
from .in_app_feed_template_param import InAppFeedTemplateParam
from .workflow_webhook_step_param import WorkflowWebhookStepParam
from .workflow_throttle_step_param import WorkflowThrottleStepParam
from .in_app_feed_channel_settings_param import InAppFeedChannelSettingsParam
from .workflow_trigger_workflow_step_param import WorkflowTriggerWorkflowStepParam

__all__ = ["WorkflowStepParam", "WorkflowInAppFeedStep"]


class WorkflowInAppFeedStep(TypedDict, total=False):
    name: Required[str]
    """A name for the workflow step."""

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


if TYPE_CHECKING or not PYDANTIC_V1:
    WorkflowStepParam = TypeAliasType(
        "WorkflowStepParam",
        Union[
            WorkflowWebhookStepParam,
            WorkflowInAppFeedStep,
            WorkflowChatStepParam,
            WorkflowSMSStepParam,
            WorkflowPushStepParam,
            WorkflowEmailStepParam,
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
        WorkflowWebhookStepParam,
        WorkflowInAppFeedStep,
        WorkflowChatStepParam,
        WorkflowSMSStepParam,
        WorkflowPushStepParam,
        WorkflowEmailStepParam,
        WorkflowDelayStepParam,
        WorkflowBatchStepParam,
        WorkflowFetchStepParam,
        WorkflowThrottleStepParam,
        "WorkflowBranchStepParam",
        WorkflowTriggerWorkflowStepParam,
    ]

from .workflow_branch_step_param import WorkflowBranchStepParam
