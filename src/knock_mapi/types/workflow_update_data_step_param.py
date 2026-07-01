# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowUpdateDataStepParam", "Settings"]


class Settings(TypedDict, total=False):
    """The settings for the update data step."""

    data: Required[str]
    """
    A JSON string or Liquid template that evaluates to the data to merge into the
    workflow's data scope.
    """


class WorkflowUpdateDataStepParam(TypedDict, total=False):
    """An update data function step.

    Merges data into the workflow's `data` scope for use in subsequent steps.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[Settings]
    """The settings for the update data step."""

    type: Required[Literal["update_data"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""
