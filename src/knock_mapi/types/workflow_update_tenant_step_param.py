# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .condition_group_param import ConditionGroupParam

__all__ = ["WorkflowUpdateTenantStepParam", "Settings"]


class Settings(TypedDict, total=False):
    """The settings for the update tenant step."""

    recipient_mode: Required[Literal["current", "reference"]]
    """The recipient mode determining how the tenant is selected.

    'current' uses the workflow's current tenant. 'reference' uses a specific tenant
    ID.
    """

    update_properties: Required[str]
    """
    A JSON string or Liquid template that evaluates to the properties to update on
    the tenant.
    """

    recipient_gid: Optional[str]
    """The global identifier (GID) of the tenant to update.

    Required when recipient_mode is 'reference'. Format: gid://Object/$tenants/{id}
    """


class WorkflowUpdateTenantStepParam(TypedDict, total=False):
    """An update tenant step.

    Updates properties of a specific tenant referenced in the workflow.
    """

    ref: Required[str]
    """The reference key of the workflow step. Must be unique per workflow."""

    settings: Required[Settings]
    """The settings for the update tenant step."""

    type: Required[Literal["update_tenant"]]
    """The type of the workflow step."""

    conditions: Optional[ConditionGroupParam]
    """A group of conditions to be evaluated."""

    description: Optional[str]
    """An arbitrary string attached to a workflow step.

    Useful for adding notes about the workflow for internal purposes.
    """

    name: Optional[str]
    """A name for the workflow step."""
