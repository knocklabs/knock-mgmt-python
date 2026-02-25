# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .condition_group import ConditionGroup

__all__ = ["WorkflowUpdateObjectStep", "Settings"]


class Settings(BaseModel):
    """The settings for the update object step."""

    recipient_gid: str
    """The global identifier (GID) of the object to update.

    Format: gid://Object/{collection}/{id}
    """

    update_properties: str
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the object.
    """


class WorkflowUpdateObjectStep(BaseModel):
    """An update object step.

    Updates properties of a specific object referenced in the workflow.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Settings
    """The settings for the update object step."""

    type: Literal["update_object"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""
