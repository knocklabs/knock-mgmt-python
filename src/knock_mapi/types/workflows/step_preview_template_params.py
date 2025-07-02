# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "StepPreviewTemplateParams",
    "Recipient",
    "RecipientObjectRecipientReference",
    "Actor",
    "ActorObjectRecipientReference",
]


class StepPreviewTemplateParams(TypedDict, total=False):
    workflow_key: Required[str]

    environment: Required[str]
    """The environment slug."""

    recipient: Required[Recipient]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    actor: Optional[Actor]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    data: Dict[str, object]
    """The data to pass to the workflow template for rendering."""

    tenant: Optional[str]
    """The tenant to associate the workflow with."""


class RecipientObjectRecipientReference(TypedDict, total=False):
    id: Required[str]

    collection: Required[str]


Recipient: TypeAlias = Union[str, RecipientObjectRecipientReference]


class ActorObjectRecipientReference(TypedDict, total=False):
    id: Required[str]

    collection: Required[str]


Actor: TypeAlias = Union[str, ActorObjectRecipientReference]
