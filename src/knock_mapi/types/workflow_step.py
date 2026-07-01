# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .duration import Duration
from .condition import Condition
from .condition_group import ConditionGroup
from .workflow_sms_step import WorkflowSMSStep
from .workflow_chat_step import WorkflowChatStep
from .workflow_push_step import WorkflowPushStep
from .workflow_batch_step import WorkflowBatchStep
from .workflow_delay_step import WorkflowDelayStep
from .workflow_email_step import WorkflowEmailStep
from .workflow_fetch_step import WorkflowFetchStep
from .workflow_webhook_step import WorkflowWebhookStep
from .workflow_ai_agent_step import WorkflowAIAgentStep
from .workflow_throttle_step import WorkflowThrottleStep
from .workflow_in_app_feed_step import WorkflowInAppFeedStep
from .workflow_update_data_step import WorkflowUpdateDataStep
from .workflow_update_user_step import WorkflowUpdateUserStep
from .workflow_random_cohort_step import WorkflowRandomCohortStep
from .workflow_update_object_step import WorkflowUpdateObjectStep
from .workflow_update_tenant_step import WorkflowUpdateTenantStep
from .workflow_trigger_workflow_step import WorkflowTriggerWorkflowStep

__all__ = [
    "WorkflowStep",
    "WorkflowWaitForEventStep",
    "WorkflowWaitForEventStepSettings",
    "WorkflowWaitForEventStepSettingsEvent",
    "WorkflowWaitForEventStepSettingsMatchCondition",
]


class WorkflowWaitForEventStepSettingsEvent(BaseModel):
    """An integration source event to wait for."""

    event_key: str
    """The name of the event to wait for."""

    event_type: Literal["integration_source"]
    """The type of event to wait for."""

    integration_source_key: str
    """The key of the integration source that emits the event to wait for."""


class WorkflowWaitForEventStepSettingsMatchCondition(BaseModel):
    conditions: Optional[List[Condition]] = None
    """A list of conditions."""

    operator: Optional[Literal["and"]] = None
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettings(BaseModel):
    """The settings for the wait for event step."""

    event: WorkflowWaitForEventStepSettingsEvent
    """An integration source event to wait for."""

    expires_after: Optional[Duration] = None
    """A duration of time, represented as a unit and a value."""

    match_conditions: Optional[List[WorkflowWaitForEventStepSettingsMatchCondition]] = None
    """A list of condition groups the incoming event must match to resolve the wait."""

    on_match: Optional[Literal["continue", "halt"]] = None
    """The action to take when a matching event is received."""

    on_timeout: Optional[Literal["continue", "halt"]] = None
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStep(BaseModel):
    """
    A wait for event function step that pauses a workflow until a matching event is received.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: WorkflowWaitForEventStepSettings
    """The settings for the wait for event step."""

    type: Literal["wait_for_event"]
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
            WorkflowAIAgentStep,
            WorkflowDelayStep,
            WorkflowWaitForEventStep,
            WorkflowBatchStep,
            WorkflowFetchStep,
            WorkflowUpdateDataStep,
            WorkflowUpdateObjectStep,
            WorkflowUpdateTenantStep,
            WorkflowUpdateUserStep,
            WorkflowThrottleStep,
            "WorkflowBranchStep",
            WorkflowRandomCohortStep,
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
        WorkflowAIAgentStep,
        WorkflowDelayStep,
        WorkflowWaitForEventStep,
        WorkflowBatchStep,
        WorkflowFetchStep,
        WorkflowUpdateDataStep,
        WorkflowUpdateObjectStep,
        WorkflowUpdateTenantStep,
        WorkflowUpdateUserStep,
        WorkflowThrottleStep,
        "WorkflowBranchStep",
        WorkflowRandomCohortStep,
        WorkflowTriggerWorkflowStep,
    ]

from .workflow_branch_step import WorkflowBranchStep
