# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommitCommitAllParams"]


class CommitCommitAllParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    commit_message: str
    """An optional message to include in a commit."""
