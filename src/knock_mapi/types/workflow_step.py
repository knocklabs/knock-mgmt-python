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
    "WorkflowWaitForEventStepSettingsUnionMember0",
    "WorkflowWaitForEventStepSettingsUnionMember0Event",
    "WorkflowWaitForEventStepSettingsUnionMember0MatchCondition",
    "WorkflowWaitForEventStepSettingsUnionMember1",
    "WorkflowWaitForEventStepSettingsUnionMember1Event",
    "WorkflowWaitForEventStepSettingsUnionMember1MatchCondition",
    "WorkflowWaitForEventStepSettingsUnionMember2",
    "WorkflowWaitForEventStepSettingsUnionMember2Event",
    "WorkflowWaitForEventStepSettingsUnionMember2MatchCondition",
    "WorkflowWaitForEventStepSettingsUnionMember3",
    "WorkflowWaitForEventStepSettingsUnionMember3Event",
    "WorkflowWaitForEventStepSettingsUnionMember3MatchCondition",
    "WorkflowWaitForEventStepSettingsUnionMember4",
    "WorkflowWaitForEventStepSettingsUnionMember4Event",
    "WorkflowWaitForEventStepSettingsUnionMember4MatchCondition",
]


class WorkflowWaitForEventStepSettingsUnionMember0Event(BaseModel):
    """An integration source event to wait for."""

    event_key: str
    """The name of the event to wait for."""

    event_type: Literal["integration_source"]
    """The type of event to wait for."""

    integration_source_key: str
    """The key of the integration source that emits the event to wait for."""


class WorkflowWaitForEventStepSettingsUnionMember0MatchCondition(BaseModel):
    conditions: Optional[List[Condition]] = None
    """A list of conditions."""

    operator: Optional[Literal["and"]] = None
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember0(BaseModel):
    """Settings for waiting on an integration source event."""

    event: WorkflowWaitForEventStepSettingsUnionMember0Event
    """An integration source event to wait for."""

    expires_after: Optional[Duration] = None
    """A duration of time, represented as a unit and a value."""

    match_conditions: Optional[List[WorkflowWaitForEventStepSettingsUnionMember0MatchCondition]] = None
    """A list of condition groups the incoming event must match to resolve the wait."""

    on_match: Optional[Literal["continue", "halt"]] = None
    """The action to take when a matching event is received."""

    on_timeout: Optional[Literal["continue", "halt"]] = None
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStepSettingsUnionMember1Event(BaseModel):
    """A message event to wait for from a message source."""

    event_key: Literal[
        "created",
        "queued",
        "sent",
        "not_sent",
        "delivered",
        "delivery_attempted",
        "undelivered",
        "bounced",
        "read",
        "unread",
        "seen",
        "unseen",
        "archived",
        "unarchived",
        "interacted",
        "link_clicked",
    ]
    """The message lifecycle event to wait for."""

    event_type: Literal["message"]
    """The type of event to wait for."""

    source_key: str
    """The key of the message source to scope the wait to."""

    source_type: Literal["workflow", "broadcast", "guide"]
    """The type of message source to scope the wait to."""


class WorkflowWaitForEventStepSettingsUnionMember1MatchCondition(BaseModel):
    conditions: Optional[List[Condition]] = None
    """A list of conditions."""

    operator: Optional[Literal["and"]] = None
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember1(BaseModel):
    """Settings for waiting on a message event."""

    event: WorkflowWaitForEventStepSettingsUnionMember1Event
    """A message event to wait for from a message source."""

    match_conditions: List[WorkflowWaitForEventStepSettingsUnionMember1MatchCondition]
    """Required when waiting for a message event.

    A list of condition groups the incoming event must match to resolve the wait.
    """

    expires_after: Optional[Duration] = None
    """A duration of time, represented as a unit and a value."""

    on_match: Optional[Literal["continue", "halt"]] = None
    """The action to take when a matching event is received."""

    on_timeout: Optional[Literal["continue", "halt"]] = None
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStepSettingsUnionMember2Event(BaseModel):
    """
    A workflow lifecycle event to wait for from a child workflow run for the same recipient.
    """

    event_key: Literal["started", "completed"]
    """The workflow lifecycle event to wait for."""

    event_type: Literal["workflow"]
    """The type of event to wait for."""

    source_key: str
    """The key of the workflow whose lifecycle event should match this wait."""


class WorkflowWaitForEventStepSettingsUnionMember2MatchCondition(BaseModel):
    conditions: Optional[List[Condition]] = None
    """A list of conditions."""

    operator: Optional[Literal["and"]] = None
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember2(BaseModel):
    """Settings for waiting on a workflow event."""

    event: WorkflowWaitForEventStepSettingsUnionMember2Event
    """
    A workflow lifecycle event to wait for from a child workflow run for the same
    recipient.
    """

    match_conditions: List[WorkflowWaitForEventStepSettingsUnionMember2MatchCondition]
    """Required when waiting for a workflow event.

    A list of condition groups the incoming event must match to resolve the wait.
    """

    expires_after: Optional[Duration] = None
    """A duration of time, represented as a unit and a value."""

    on_match: Optional[Literal["continue", "halt"]] = None
    """The action to take when a matching event is received."""

    on_timeout: Optional[Literal["continue", "halt"]] = None
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStepSettingsUnionMember3Event(BaseModel):
    """
    An audience membership event to wait for when a recipient enters or exits an audience.
    """

    audience_key: str
    """The key of the audience to wait for membership changes."""

    event_key: Literal["enter", "exit"]
    """The audience membership transition to wait for."""

    event_type: Literal["audience"]
    """The type of event to wait for."""


class WorkflowWaitForEventStepSettingsUnionMember3MatchCondition(BaseModel):
    conditions: Optional[List[Condition]] = None
    """A list of conditions."""

    operator: Optional[Literal["and"]] = None
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember3(BaseModel):
    """Settings for waiting on an audience membership event."""

    event: WorkflowWaitForEventStepSettingsUnionMember3Event
    """
    An audience membership event to wait for when a recipient enters or exits an
    audience.
    """

    expires_after: Optional[Duration] = None
    """A duration of time, represented as a unit and a value."""

    match_conditions: Optional[List[WorkflowWaitForEventStepSettingsUnionMember3MatchCondition]] = None
    """A list of condition groups the incoming event must match to resolve the wait."""

    on_match: Optional[Literal["continue", "halt"]] = None
    """The action to take when a matching event is received."""

    on_timeout: Optional[Literal["continue", "halt"]] = None
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStepSettingsUnionMember4Event(BaseModel):
    """A recipient updated event to wait for from the workflow recipient."""

    event_type: Literal["recipient"]
    """The type of event to wait for."""

    event_key: Optional[Literal["updated"]] = None
    """Recipient lifecycle event to wait for. Always "updated" today."""


class WorkflowWaitForEventStepSettingsUnionMember4MatchCondition(BaseModel):
    conditions: Optional[List[Condition]] = None
    """A list of conditions."""

    operator: Optional[Literal["and"]] = None
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember4(BaseModel):
    """Settings for waiting on a recipient change event."""

    event: WorkflowWaitForEventStepSettingsUnionMember4Event
    """A recipient updated event to wait for from the workflow recipient."""

    expires_after: Optional[Duration] = None
    """A duration of time, represented as a unit and a value."""

    match_conditions: Optional[List[WorkflowWaitForEventStepSettingsUnionMember4MatchCondition]] = None
    """A list of condition groups the incoming event must match to resolve the wait."""

    on_match: Optional[Literal["continue", "halt"]] = None
    """The action to take when a matching event is received."""

    on_timeout: Optional[Literal["continue", "halt"]] = None
    """The action to take when the wait expires before a match."""


WorkflowWaitForEventStepSettings: TypeAlias = Union[
    WorkflowWaitForEventStepSettingsUnionMember0,
    WorkflowWaitForEventStepSettingsUnionMember1,
    WorkflowWaitForEventStepSettingsUnionMember2,
    WorkflowWaitForEventStepSettingsUnionMember3,
    WorkflowWaitForEventStepSettingsUnionMember4,
]


class WorkflowWaitForEventStep(BaseModel):
    """
    A wait for event function step that pauses a workflow until a matching event is received.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: WorkflowWaitForEventStepSettings
    """The settings for the wait for event step.

    When `event.event_type` is `message` or `workflow`, `match_conditions` is
    required.
    """

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
