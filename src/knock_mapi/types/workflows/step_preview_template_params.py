# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..shared_params.recipient_reference import RecipientReference

__all__ = ["StepPreviewTemplateParams"]


class StepPreviewTemplateParams(TypedDict, total=False):
    workflow_key: Required[str]

    environment: Required[str]
    """The environment slug."""

    recipient: Required[RecipientReference]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    actor: Optional[RecipientReference]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    data: Dict[str, object]
    """The data to pass to the workflow template for rendering."""

    tenant: Optional[str]
    """The tenant to associate the workflow with. Must not contain whitespace."""
