# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .condition_group import ConditionGroup

__all__ = ["WorkflowTriggerWorkflowStep", "Settings"]


class Settings(BaseModel):
    actor: Optional[str] = None
    """The actor to trigger the workflow with. Supports liquid."""

    cancellation_key: Optional[str] = None
    """The cancellation key to trigger the workflow with. Supports liquid."""

    data: Optional[str] = None
    """The data to be supplied to the workflow. Supports liquid."""

    recipients: Optional[str] = None
    """The recipients or recipient to trigger the workflow for. Supports liquid."""

    tenant: Optional[str] = None
    """The tenant to trigger the workflow with. Supports liquid."""

    workflow_key: Optional[str] = None
    """The key of the workflow to trigger. Supports liquid."""


class WorkflowTriggerWorkflowStep(BaseModel):
    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Settings
    """The settings for the workflow trigger workflow step."""

    type: Literal["trigger_workflow"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """A description for the workflow step."""

    name: Optional[str] = None
    """A name for the workflow step."""
