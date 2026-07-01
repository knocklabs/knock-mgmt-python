# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowUpdateObjectStepParam", "Settings"]


class Settings(TypedDict, total=False):
    """The settings for the update object step."""

    recipient_gid: Required[str]
    """The global identifier (GID) of the object to update.

    Format: gid://Object/{collection}/{id}
    """

    update_properties: Required[str]
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the object.
    """


class WorkflowUpdateObjectStepParam(TypedDict, total=False):
    """An update object step.

    Updates properties of a specific object referenced in the workflow.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[Settings]
    """The settings for the update object step."""

    type: Required[Literal["update_object"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""
