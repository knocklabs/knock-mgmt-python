# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .condition_group_param import ConditionGroupParam
from .request_template_param import RequestTemplateParam

__all__ = ["WorkflowFetchStepParam"]


class WorkflowFetchStepParam(TypedDict, total=False):
    """A fetch function step.

    Retrieves data from an external source and merges it into the workflow's `data` scope for use in later steps. Read more in the [docs](https://docs.knock.app/designing-workflows/fetch-function).
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[RequestTemplateParam]
    """A request template for a fetch function step."""

    type: Required[Literal["http_fetch"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""
