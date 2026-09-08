# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypedDict

__all__ = ["CommitCommitAllParams"]


class CommitCommitAllParams(TypedDict, total=False):
    allow_empty: bool
    """
    When used with a single resource_type and resource_id, creates a new version
    with identical content and commits it if there are no unpublished changes.
    """

    branch: str
    """The slug of a branch to use.

    When `environment` is omitted, the branch is resolved from Development after the
    account default is injected. When `environment` is supplied, it must be
    `"development"`.
    """

    commit_message: str
    """An optional message to include in a commit."""

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    resource_id: str
    """Filter changes to commit by resource identifier.

    Must be used together with resource_type.
    """

    resource_type: Union[
        Literal["audience", "email_layout", "guide", "message_type", "partial", "translation", "workflow"],
        List[Literal["audience", "email_layout", "guide", "message_type", "partial", "translation", "workflow"]],
    ]
    """Filter changes to commit by resource type(s).

    Accepts a single type or array of types. Can be combined with resource_id to
    filter for specific resources.
    """
