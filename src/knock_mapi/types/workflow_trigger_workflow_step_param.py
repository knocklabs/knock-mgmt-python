# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowTriggerWorkflowStepParam", "Settings"]


class Settings(TypedDict, total=False):
    """The settings for the workflow trigger workflow step."""

    actor: str
    """The actor to trigger the workflow with. Supports liquid."""

    cancellation_key: str
    """The cancellation key to trigger the workflow with. Supports liquid."""

    data: str
    """The data to be supplied to the workflow. Supports liquid."""

    recipients: str
    """The recipients or recipient to trigger the workflow for. Supports liquid."""

    tenant: str
    """The tenant to trigger the workflow with. Supports liquid."""

    workflow_key: str
    """The key of the workflow to trigger. Supports liquid."""


class WorkflowTriggerWorkflowStepParam(TypedDict, total=False):
    """A workflow trigger function step.

    Read more in the [docs](https://docs.knock.app/designing-workflows/trigger-workflow-function).
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[Settings]
    """The settings for the workflow trigger workflow step."""

    type: Required[Literal["trigger_workflow"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """A description for the workflow step."""

    name: Optional[str]
    """A name for the workflow step."""
