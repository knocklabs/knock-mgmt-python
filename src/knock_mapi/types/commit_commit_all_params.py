# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CommitCommitAllParams"]


class CommitCommitAllParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    commit_message: str
    """An optional message to include in a commit."""

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
