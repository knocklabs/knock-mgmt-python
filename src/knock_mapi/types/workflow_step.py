# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .send_window import SendWindow
from .condition_group import ConditionGroup
from .workflow_sms_step import WorkflowSMSStep
from .workflow_chat_step import WorkflowChatStep
from .workflow_push_step import WorkflowPushStep
from .workflow_batch_step import WorkflowBatchStep
from .workflow_delay_step import WorkflowDelayStep
from .workflow_email_step import WorkflowEmailStep
from .workflow_fetch_step import WorkflowFetchStep
from .in_app_feed_template import InAppFeedTemplate
from .workflow_webhook_step import WorkflowWebhookStep
from .workflow_throttle_step import WorkflowThrottleStep
from .in_app_feed_channel_settings import InAppFeedChannelSettings
from .workflow_trigger_workflow_step import WorkflowTriggerWorkflowStep

__all__ = ["WorkflowStep", "WorkflowInAppFeedStep"]


class WorkflowInAppFeedStep(BaseModel):
    name: str
    """A name for the workflow step."""

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
