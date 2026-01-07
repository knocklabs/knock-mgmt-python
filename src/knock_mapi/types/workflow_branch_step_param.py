# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowBranchStepParam", "Branch"]


class Branch(TypedDict, total=False):
    """A branch in a branch step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    name: str
    """The name of the branch."""

    steps: Iterable["WorkflowStepParam"]
    """A list of steps that will be executed if the branch is chosen."""

    terminates: bool
    """If the workflow should halt at the end of the branch.

    Defaults to false if not provided.
    """


class WorkflowBranchStepParam(TypedDict, total=False):
    """A branch function step.

    Read more in the [docs](https://docs.knock.app/designing-workflows/branch-function).
    """

    branches: Required[Iterable[Branch]]
    """A list of workflow branches to be evaluated."""

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    type: Required[Literal["branch"]]
    """The type of step."""

    description: str
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""


from .workflow_step_param import WorkflowStepParam
