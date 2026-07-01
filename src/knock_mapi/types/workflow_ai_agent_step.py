# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .condition_group import ConditionGroup

__all__ = ["WorkflowAIAgentStep", "Settings"]


class Settings(BaseModel):
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

    settings: Settings
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
