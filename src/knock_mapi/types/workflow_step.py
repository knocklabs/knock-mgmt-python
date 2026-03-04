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
from .workflow_update_data_step import WorkflowUpdateDataStep
from .workflow_update_user_step import WorkflowUpdateUserStep
from .workflow_random_cohort_step import WorkflowRandomCohortStep
from .workflow_update_object_step import WorkflowUpdateObjectStep
from .workflow_update_tenant_step import WorkflowUpdateTenantStep
from .workflow_trigger_workflow_step import WorkflowTriggerWorkflowStep

__all__ = ["WorkflowStep", "WorkflowAIAgentStep", "WorkflowAIAgentStepSettings"]


class WorkflowAIAgentStepSettings(BaseModel):
    """The settings for the AI agent step."""

    model: str
    """The AI model to use in `provider:model` format (e.g.

    `anthropic:claude-haiku-4-5`, `openai:gpt-5.2-chat-latest`). See the
    documentation for a list of supported models.
    """

    request_prompt: str
    """The prompt template for the AI request. Supports Liquid templating."""

    response_type: Literal["text", "json"]
    """The type of response to expect from the AI model."""

    halt_on_error: Optional[bool] = None
    """Whether to halt the workflow if the AI fetch fails."""

    response_schema: Optional[str] = None
    """A JSON schema string for structured output.

    Required when `response_type` is `json`. Must not be set when `response_type` is
    `text`.
    """

    web_search_enabled: Optional[bool] = None
    """Whether to enable web search for the AI request."""


class WorkflowAIAgentStep(BaseModel):
    """An AI agent function step.

    Fetches data from an AI model and merges it into the workflow's `data` scope for use in later steps. Supports Liquid templating in the prompt. Read more in the [docs](https://docs.knock.app/designing-workflows/ai-agent-function).
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: WorkflowAIAgentStepSettings
    """The settings for the AI agent step."""

    type: Literal["ai_agent"]
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
