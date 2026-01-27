# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "WorkflowRunParams",
    "Recipient",
    "RecipientObjectRecipientReference",
    "Actor",
    "ActorObjectRecipientReference",
]


class WorkflowRunParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    recipients: Required[SequenceNotStr[Recipient]]
    """A list of recipients to run the workflow for."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    actor: Optional[Actor]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    cancellation_key: Optional[str]
    """A key to cancel the workflow run."""

    data: Dict[str, object]
    """A map of data to be used in the workflow run.

    The structure should conform to the workflow's `trigger_data_json_schema` if one
    is defined. Available in templates as `{{ data.field_name }}`. See
    [trigger data validation docs](https://docs.knock.app/developer-tools/validating-trigger-data).
    """

    tenant: str
    """The tenant to associate the workflow run with. Must not contain whitespace."""


class RecipientObjectRecipientReference(TypedDict, total=False):
    """An object reference."""

    id: Required[str]
    """The ID of the object."""

    collection: Required[str]
    """The collection of the object."""


Recipient: TypeAlias = Union[str, RecipientObjectRecipientReference]


class ActorObjectRecipientReference(TypedDict, total=False):
    """An object reference."""

    id: Required[str]
    """The ID of the object."""

    collection: Required[str]
    """The collection of the object."""


Actor: TypeAlias = Union[str, ActorObjectRecipientReference]
