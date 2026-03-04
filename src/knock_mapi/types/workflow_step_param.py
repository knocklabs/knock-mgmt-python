# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from .._compat import PYDANTIC_V1
from .condition_group_param import ConditionGroupParam
from .workflow_sms_step_param import WorkflowSMSStepParam
from .workflow_chat_step_param import WorkflowChatStepParam
from .workflow_push_step_param import WorkflowPushStepParam
from .workflow_batch_step_param import WorkflowBatchStepParam
from .workflow_delay_step_param import WorkflowDelayStepParam
from .workflow_email_step_param import WorkflowEmailStepParam
from .workflow_fetch_step_param import WorkflowFetchStepParam
from .workflow_webhook_step_param import WorkflowWebhookStepParam
from .workflow_throttle_step_param import WorkflowThrottleStepParam
from .workflow_in_app_feed_step_param import WorkflowInAppFeedStepParam
from .workflow_update_data_step_param import WorkflowUpdateDataStepParam
from .workflow_update_user_step_param import WorkflowUpdateUserStepParam
from .workflow_random_cohort_step_param import WorkflowRandomCohortStepParam
from .workflow_update_object_step_param import WorkflowUpdateObjectStepParam
from .workflow_update_tenant_step_param import WorkflowUpdateTenantStepParam
from .workflow_trigger_workflow_step_param import WorkflowTriggerWorkflowStepParam

__all__ = ["WorkflowStepParam", "WorkflowAIAgentStep", "WorkflowAIAgentStepSettings"]


class WorkflowAIAgentStepSettings(TypedDict, total=False):
    """The settings for the AI agent step."""

    model: Required[str]
    """The AI model to use in `provider:model` format (e.g.

    `anthropic:claude-haiku-4-5`, `openai:gpt-5.2-chat-latest`). See the
    documentation for a list of supported models.
    """

    request_prompt: Required[str]
    """The prompt template for the AI request. Supports Liquid templating."""

    response_type: Required[Literal["text", "json"]]
    """The type of response to expect from the AI model."""

    halt_on_error: Optional[bool]
    """Whether to halt the workflow if the AI fetch fails."""

    response_schema: Optional[str]
    """A JSON schema string for structured output.

    Required when `response_type` is `json`. Must not be set when `response_type` is
    `text`.
    """

    web_search_enabled: Optional[bool]
    """Whether to enable web search for the AI request."""


class WorkflowAIAgentStep(TypedDict, total=False):
    """An AI agent function step.

    Fetches data from an AI model and merges it into the workflow's `data` scope for use in later steps. Supports Liquid templating in the prompt. Read more in the [docs](https://docs.knock.app/designing-workflows/ai-agent-function).
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[WorkflowAIAgentStepSettings]
    """The settings for the AI agent step."""

    type: Required[Literal["ai_agent"]]
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
            WorkflowAIAgentStep,
            WorkflowDelayStepParam,
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
        WorkflowAIAgentStep,
        WorkflowDelayStepParam,
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
