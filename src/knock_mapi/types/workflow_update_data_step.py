# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .condition_group import ConditionGroup

__all__ = ["WorkflowUpdateDataStep", "Settings"]


class Settings(BaseModel):
    """The settings for the update data step."""

    data: str
    """
    A JSON string or Liquid template that evaluates to the data to merge into the
    workflow's data scope.
    """


class WorkflowUpdateDataStep(BaseModel):
    """An update data function step.

    Merges data into the workflow's `data` scope for use in subsequent steps.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Settings
    """The settings for the update data step."""

    type: Literal["update_data"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""
