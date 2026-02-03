# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .condition_group import ConditionGroup
from .workflow_sms_step import WorkflowSMSStep
from .workflow_chat_step import WorkflowChatStep
from .workflow_push_step import WorkflowPushStep
from .workflow_batch_step import WorkflowBatchStep
from .workflow_delay_step import WorkflowDelayStep
from .workflow_email_step import WorkflowEmailStep
from .workflow_fetch_step import WorkflowFetchStep
from .workflow_webhook_step import WorkflowWebhookStep
from .workflow_throttle_step import WorkflowThrottleStep
from .workflow_in_app_feed_step import WorkflowInAppFeedStep
from .workflow_trigger_workflow_step import WorkflowTriggerWorkflowStep

__all__ = ["WorkflowStep", "WorkflowUpdateDataStep", "WorkflowUpdateDataStepSettings"]


class WorkflowUpdateDataStepSettings(BaseModel):
    """The settings for the update data step."""

    data: str
    """
    A JSON string or Liquid template that evaluates to the data to merge into the
    workflow's data scope.
    """


class WorkflowUpdateDataStep(BaseModel):
    """An update data function step.

    Merges data into the workflow's `data` scope for use in subsequent steps.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: WorkflowUpdateDataStepSettings
    """The settings for the update data step."""

    type: Literal["update_data"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""


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
            WorkflowUpdateDataStep,
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
        WorkflowUpdateDataStep,
        WorkflowThrottleStep,
        "WorkflowBranchStep",
        WorkflowTriggerWorkflowStep,
    ]

from .workflow_branch_step import WorkflowBranchStep
