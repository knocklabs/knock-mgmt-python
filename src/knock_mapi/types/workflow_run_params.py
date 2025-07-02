# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["WorkflowRunParams", "Recipient", "RecipientUnionMember1", "Actor", "ActorUnionMember1"]


class WorkflowRunParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    recipients: Required[List[Recipient]]
    """A list of recipients to run the workflow for."""

    actor: Optional[Actor]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    cancellation_key: Optional[str]
    """A key to cancel the workflow run."""

    data: Dict[str, object]
    """A map of data to be used in the workflow run."""

    tenant: str
    """The tenant to associate the workflow run with."""


class RecipientUnionMember1(TypedDict, total=False):
    id: Required[str]

    collection: Required[str]


Recipient: TypeAlias = Union[str, RecipientUnionMember1]


class ActorUnionMember1(TypedDict, total=False):
    id: Required[str]

    collection: Required[str]


Actor: TypeAlias = Union[str, ActorUnionMember1]
