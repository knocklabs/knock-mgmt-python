# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowAIAgentStepParam", "Settings"]


class Settings(TypedDict, total=False):
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


class WorkflowAIAgentStepParam(TypedDict, total=False):
    """An AI agent function step.

    Fetches data from an AI model and merges it into the workflow's `data` scope for use in later steps. Supports Liquid templating in the prompt. Read more in the [docs](https://docs.knock.app/designing-workflows/ai-agent-function).
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[Settings]
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
