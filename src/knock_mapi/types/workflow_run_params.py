# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "WorkflowRunParams",
    "Recipient",
    "RecipientObjectRecipientReference",
    "RecipientInlineIdentifyUserRequest",
    "Actor",
    "ActorObjectRecipientReference",
    "ActorInlineIdentifyUserRequest",
]


class WorkflowRunParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    recipients: Required[SequenceNotStr[Recipient]]
    """A list of recipients to run the workflow for.

    Supports user IDs, object references, or inline identify user objects (id +
    optional email/name).
    """

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    actor: Optional[Actor]
    """The actor to reference in the the workflow run."""

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


class RecipientInlineIdentifyUserRequest(TypedDict, total=False):
    """A user recipient with optional identify properties.

    When email or name are provided, the user is created or updated as part of the workflow run. The collection is always `$users` and should not be sent.
    """

    id: Required[str]
    """The ID of the user."""

    email: Optional[str]
    """The email address to set on the user."""

    name: Optional[str]
    """The display name to set on the user."""


Recipient: TypeAlias = Union[str, RecipientObjectRecipientReference, RecipientInlineIdentifyUserRequest]


class ActorObjectRecipientReference(TypedDict, total=False):
    """An object reference."""

    id: Required[str]
    """The ID of the object."""

    collection: Required[str]
    """The collection of the object."""


class ActorInlineIdentifyUserRequest(TypedDict, total=False):
    """A user recipient with optional identify properties.

    When email or name are provided, the user is created or updated as part of the workflow run. The collection is always `$users` and should not be sent.
    """

    id: Required[str]
    """The ID of the user."""

    email: Optional[str]
    """The email address to set on the user."""

    name: Optional[str]
    """The display name to set on the user."""


Actor: TypeAlias = Union[str, ActorObjectRecipientReference, ActorInlineIdentifyUserRequest]
