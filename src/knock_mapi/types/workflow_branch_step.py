# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .condition_group import ConditionGroup

__all__ = ["WorkflowBranchStep", "Branch"]


class Branch(BaseModel):
    """A branch in a branch step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    name: Optional[str] = None
    """The name of the branch."""

    steps: Optional[List["WorkflowStep"]] = None
    """A list of steps that will be executed if the branch is chosen."""

    terminates: Optional[bool] = None
    """If the workflow should halt at the end of the branch."""


class WorkflowBranchStep(BaseModel):
    """A branch function step.

    Read more in the [docs](https://docs.knock.app/designing-workflows/branch-function).
    """

    branches: List[Branch]
    """A list of workflow branches to be evaluated."""

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    type: Literal["branch"]
    """The type of step."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""


from .workflow_step import WorkflowStep
