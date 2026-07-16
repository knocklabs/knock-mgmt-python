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


class WorkflowWaitForEventStepSettingsUnionMember0Event(TypedDict, total=False):
    """An integration source event to wait for."""

    event_key: Required[str]
    """The name of the event to wait for."""

    event_type: Required[Literal["integration_source"]]
    """The type of event to wait for."""

    integration_source_key: Required[str]
    """The key of the integration source that emits the event to wait for."""


class WorkflowWaitForEventStepSettingsUnionMember0MatchCondition(TypedDict, total=False):
    conditions: Iterable[ConditionParam]
    """A list of conditions."""

    operator: Literal["and"]
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember0(TypedDict, total=False):
    """Settings for waiting on an integration source event."""

    event: Required[WorkflowWaitForEventStepSettingsUnionMember0Event]
    """An integration source event to wait for."""

    expires_after: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    match_conditions: Iterable[WorkflowWaitForEventStepSettingsUnionMember0MatchCondition]
    """A list of condition groups the incoming event must match to resolve the wait."""

    on_match: Literal["continue", "halt"]
    """The action to take when a matching event is received."""

    on_timeout: Literal["continue", "halt"]
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStepSettingsUnionMember1Event(TypedDict, total=False):
    """A message event to wait for from a message source."""

    event_key: Required[
        Literal[
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
    ]
    """The message lifecycle event to wait for."""

    event_type: Required[Literal["message"]]
    """The type of event to wait for."""

    source_key: Required[str]
    """The key of the message source to scope the wait to."""

    source_type: Required[Literal["workflow", "broadcast", "guide"]]
    """The type of message source to scope the wait to."""


class WorkflowWaitForEventStepSettingsUnionMember1MatchCondition(TypedDict, total=False):
    conditions: Iterable[ConditionParam]
    """A list of conditions."""

    operator: Literal["and"]
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember1(TypedDict, total=False):
    """Settings for waiting on a message event."""

    event: Required[WorkflowWaitForEventStepSettingsUnionMember1Event]
    """A message event to wait for from a message source."""

    match_conditions: Required[Iterable[WorkflowWaitForEventStepSettingsUnionMember1MatchCondition]]
    """Required when waiting for a message event.

    A list of condition groups the incoming event must match to resolve the wait.
    """

    expires_after: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    on_match: Literal["continue", "halt"]
    """The action to take when a matching event is received."""

    on_timeout: Literal["continue", "halt"]
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStepSettingsUnionMember2Event(TypedDict, total=False):
    """
    A workflow lifecycle event to wait for from a child workflow run for the same recipient.
    """

    event_key: Required[Literal["started", "completed"]]
    """The workflow lifecycle event to wait for."""

    event_type: Required[Literal["workflow"]]
    """The type of event to wait for."""

    source_key: Required[str]
    """The key of the workflow whose lifecycle event should match this wait."""


class WorkflowWaitForEventStepSettingsUnionMember2MatchCondition(TypedDict, total=False):
    conditions: Iterable[ConditionParam]
    """A list of conditions."""

    operator: Literal["and"]
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember2(TypedDict, total=False):
    """Settings for waiting on a workflow event."""

    event: Required[WorkflowWaitForEventStepSettingsUnionMember2Event]
    """
    A workflow lifecycle event to wait for from a child workflow run for the same
    recipient.
    """

    match_conditions: Required[Iterable[WorkflowWaitForEventStepSettingsUnionMember2MatchCondition]]
    """Required when waiting for a workflow event.

    A list of condition groups the incoming event must match to resolve the wait.
    """

    expires_after: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    on_match: Literal["continue", "halt"]
    """The action to take when a matching event is received."""

    on_timeout: Literal["continue", "halt"]
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStepSettingsUnionMember3Event(TypedDict, total=False):
    """
    An audience membership event to wait for when a recipient enters or exits an audience.
    """

    audience_key: Required[str]
    """The key of the audience to wait for membership changes."""

    event_key: Required[Literal["enter", "exit"]]
    """The audience membership transition to wait for."""

    event_type: Required[Literal["audience"]]
    """The type of event to wait for."""


class WorkflowWaitForEventStepSettingsUnionMember3MatchCondition(TypedDict, total=False):
    conditions: Iterable[ConditionParam]
    """A list of conditions."""

    operator: Literal["and"]
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember3(TypedDict, total=False):
    """Settings for waiting on an audience membership event."""

    event: Required[WorkflowWaitForEventStepSettingsUnionMember3Event]
    """
    An audience membership event to wait for when a recipient enters or exits an
    audience.
    """

    expires_after: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    match_conditions: Iterable[WorkflowWaitForEventStepSettingsUnionMember3MatchCondition]
    """A list of condition groups the incoming event must match to resolve the wait."""

    on_match: Literal["continue", "halt"]
    """The action to take when a matching event is received."""

    on_timeout: Literal["continue", "halt"]
    """The action to take when the wait expires before a match."""


class WorkflowWaitForEventStepSettingsUnionMember4Event(TypedDict, total=False):
    """A recipient updated event to wait for from the workflow recipient."""

    event_type: Required[Literal["recipient"]]
    """The type of event to wait for."""

    event_key: Literal["updated"]
    """Recipient lifecycle event to wait for. Always "updated" today."""


class WorkflowWaitForEventStepSettingsUnionMember4MatchCondition(TypedDict, total=False):
    conditions: Iterable[ConditionParam]
    """A list of conditions."""

    operator: Literal["and"]
    """The operator used to join the conditions in the group."""


class WorkflowWaitForEventStepSettingsUnionMember4(TypedDict, total=False):
    """Settings for waiting on a recipient change event."""

    event: Required[WorkflowWaitForEventStepSettingsUnionMember4Event]
    """A recipient updated event to wait for from the workflow recipient."""

    expires_after: Optional[DurationParam]
    """A duration of time, represented as a unit and a value."""

    match_conditions: Iterable[WorkflowWaitForEventStepSettingsUnionMember4MatchCondition]
    """A list of condition groups the incoming event must match to resolve the wait."""

    on_match: Literal["continue", "halt"]
    """The action to take when a matching event is received."""

    on_timeout: Literal["continue", "halt"]
    """The action to take when the wait expires before a match."""


WorkflowWaitForEventStepSettings: TypeAlias = Union[
    WorkflowWaitForEventStepSettingsUnionMember0,
    WorkflowWaitForEventStepSettingsUnionMember1,
    WorkflowWaitForEventStepSettingsUnionMember2,
    WorkflowWaitForEventStepSettingsUnionMember3,
    WorkflowWaitForEventStepSettingsUnionMember4,
]


class WorkflowWaitForEventStep(TypedDict, total=False):
    """
    A wait for event function step that pauses a workflow until a matching event is received.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[WorkflowWaitForEventStepSettings]
    """The settings for the wait for event step.

    When `event.event_type` is `message` or `workflow`, `match_conditions` is
    required.
    """

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
