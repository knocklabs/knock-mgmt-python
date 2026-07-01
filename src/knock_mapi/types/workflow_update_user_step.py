# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .condition_group import ConditionGroup

__all__ = ["WorkflowUpdateUserStep", "Settings"]


class Settings(BaseModel):
    """The settings for the update user step."""

    recipient_mode: Literal["current", "reference"]
    """The recipient mode determining how the user is selected.

    'current' uses the workflow's current user. 'reference' uses a specific user ID.
    """

    update_properties: str
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the user.
    """

    recipient_gid: Optional[str] = None
    """The global identifier (GID) of the user to update.

    Required when recipient_mode is 'reference'. Format: gid://Object/$users/{id}
    """


class WorkflowUpdateUserStep(BaseModel):
    """An update user step.

    Updates properties of a specific user referenced in the workflow.
    """

    ref: str
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Settings
    """The settings for the update user step."""

    type: Literal["update_user"]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroup] = None
    """A group of conditions to be evaluated."""

    description: Optional[str] = None
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str] = None
    """A name for the workflow step."""
