# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from .._compat import PYDANTIC_V1
from .duration_param import DurationParam
from .condition_param import ConditionParam
from .condition_group_param import ConditionGroupParam
from .workflow_sms_step_param import WorkflowSMSStepParam
from .workflow_chat_step_param import WorkflowChatStepParam
from .workflow_push_step_param import WorkflowPushStepParam
from .workflow_batch_step_param import WorkflowBatchStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam
from .workflow_email_step_param import WorkflowEmailStepParam
from .workflow_fetch_step_param import WorkflowFetchStepParam
from .workflow_webhook_step_param import WorkflowWebhookStepParam
from .workflow_ai_agent_step_param import WorkflowAIAgentStepParam
from .workflow_throttle_step_param import WorkflowThrottleStepParam
from .workflow_in_app_feed_step_param import WorkflowInAppFeedStepParam
from .workflow_update_data_step_param import WorkflowUpdateDataStepParam
from .workflow_update_user_step_param import WorkflowUpdateUserStepParam
from .workflow_random_cohort_step_param import WorkflowRandomCohortStepParam
from .workflow_update_object_step_param import WorkflowUpdateObjectStepParam
from .workflow_update_tenant_step_param import WorkflowUpdateTenantStepParam
from .workflow_trigger_workflow_step_param import WorkflowTriggerWorkflowStepParam

__all__ = [
    "WorkflowStepParam",
    "WorkflowWaitForEventStep",
    "WorkflowWaitForEventStepSettings",
    "WorkflowWaitForEventStepSettingsEvent",
    "WorkflowWaitForEventStepSettingsMatchCondition",
]


class WorkflowWaitForEventStepSettingsEvent(TypedDict, total=False):
    """An integration source event to wait for."""

    event_key: Required[str]
    """The name of the event to wait for."""

    event_type: Required[Literal["integration_source"]]
    """The type of event to wait for."""

    integration_source_key: Required[str]
    """The key of the integration source that emits the event to wait for."""


class WorkflowWaitForEventStepSettingsMatchCondition(TypedDict, total=False):
    conditions: Iterable[ConditionParam]
    """A list of conditions."""

    operator: Literal["and"]
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettings(TypedDict, total=False):
    """The settings for the wait for event step."""

    event: Required[WorkflowWaitForEventStepSettingsEvent]
    """An integration source event to wait for."""

    expires_after: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    match_conditions: Iterable[WorkflowWaitForEventStepSettingsMatchCondition]
    """A list of condition groups the incoming event must match to resolve the wait."""

    on_match: Literal["continue", "halt"]
    """The action to take when a matching event is received."""

    on_timeout: Literal["continue", "halt"]
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStep(TypedDict, total=False):
    """
    A wait for event function step that pauses a workflow until a matching event is received.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[WorkflowWaitForEventStepSettings]
    """The settings for the wait for event step."""

    type: Required[Literal["wait_for_event"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""


if TYPE_CHECKING or not PYDANTIC_V1:
    WorkflowStepParam = TypeAliasType(
        "WorkflowStepParam",
        Union[
            WorkflowWebhookStepParam,
            WorkflowInAppFeedStepParam,
            WorkflowChatStepParam,
            WorkflowSMSStepParam,
            WorkflowPushStepParam,
            WorkflowEmailStepParam,
            WorkflowAIAgentStepParam,
            WorkflowDelayStepParam,
            WorkflowWaitForEventStep,
            WorkflowBatchStepParam,
            WorkflowFetchStepParam,
            WorkflowUpdateDataStepParam,
            WorkflowUpdateObjectStepParam,
            WorkflowUpdateTenantStepParam,
            WorkflowUpdateUserStepParam,
            WorkflowThrottleStepParam,
            "WorkflowBranchStepParam",
            WorkflowRandomCohortStepParam,
            WorkflowTriggerWorkflowStepParam,
        ],
    )
else:
    WorkflowStepParam: TypeAlias = Union[
        WorkflowWebhookStepParam,
        WorkflowInAppFeedStepParam,
        WorkflowChatStepParam,
        WorkflowSMSStepParam,
        WorkflowPushStepParam,
        WorkflowEmailStepParam,
        WorkflowAIAgentStepParam,
        WorkflowDelayStepParam,
        WorkflowWaitForEventStep,
        WorkflowBatchStepParam,
        WorkflowFetchStepParam,
        WorkflowUpdateDataStepParam,
        WorkflowUpdateObjectStepParam,
        WorkflowUpdateTenantStepParam,
        WorkflowUpdateUserStepParam,
        WorkflowThrottleStepParam,
        "WorkflowBranchStepParam",
        WorkflowRandomCohortStepParam,
        WorkflowTriggerWorkflowStepParam,
    ]

from .workflow_branch_step_param import WorkflowBranchStepParam
