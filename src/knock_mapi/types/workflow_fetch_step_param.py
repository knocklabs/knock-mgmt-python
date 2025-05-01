# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .condition_group_param import ConditionGroupParam
from .request_template_param import RequestTemplateParam

__all__ = ["WorkflowFetchStepParam"]


class WorkflowFetchStepParam(TypedDict, total=False):
    name: Required[str]
    """A name for the workflow step."""

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[RequestTemplateParam]
    """A request template for a fetch function step."""

    type: Required[Literal["fetch"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """
