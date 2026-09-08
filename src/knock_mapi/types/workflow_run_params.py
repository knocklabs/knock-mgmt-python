# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .inline_identify_user_request_param import InlineIdentifyUserRequestParam

__all__ = [
    "WorkflowRunParams",
    "Recipient",
    "RecipientObjectRecipientReference",
    "Actor",
    "ActorObjectRecipientReference",
]


class WorkflowRunParams(TypedDict, total=False):
    recipients: Required[SequenceNotStr[Recipient]]
    """A list of recipients to run the workflow for.

    Supports user IDs, object references, or inline identify user objects (id +
    optional email/name).
    """

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

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


Recipient: TypeAlias = Union[str, RecipientObjectRecipientReference, InlineIdentifyUserRequestParam]


class ActorObjectRecipientReference(TypedDict, total=False):
    """An object reference."""

    id: Required[str]
    """The ID of the object."""

    collection: Required[str]
    """The collection of the object."""


Actor: TypeAlias = Union[str, ActorObjectRecipientReference, InlineIdentifyUserRequestParam]
