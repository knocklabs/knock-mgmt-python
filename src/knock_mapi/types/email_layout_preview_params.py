# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .email_layout_request_param import EmailLayoutRequestParam
from .shared_params.recipient_reference import RecipientReference

__all__ = ["EmailLayoutPreviewParams", "Workflow"]


class EmailLayoutPreviewParams(TypedDict, total=False):
    email_layout: Required[EmailLayoutRequestParam]
    """A request to update or create an email layout."""

    recipient: Required[RecipientReference]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    actor: Optional[RecipientReference]
    """
    A recipient reference, used when referencing a recipient by either their ID (for
    a user), or by a reference for an object.
    """

    data: Dict[str, object]
    """The data to pass to the layout for rendering."""

    tenant: Optional[str]
    """The tenant to associate with the preview. Must not contain whitespace."""

    workflow: Optional[Workflow]
    """Optional workflow context for variable hydration.

    When provided, recipient/actor/tenant are resolved via Knock.
    """


class Workflow(TypedDict, total=False):
    """Optional workflow context for variable hydration.

    When provided, recipient/actor/tenant are resolved via Knock.
    """

    key: Required[str]
    """The workflow key."""

    categories: Optional[SequenceNotStr[str]]
    """Workflow categories."""
