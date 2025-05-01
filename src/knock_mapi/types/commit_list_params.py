# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommitListParams"]


class CommitListParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    limit: int
    """The number of entries to fetch per-page."""

    promoted: bool
    """
    Whether to show commits in the given environment that have not been promoted to
    the subsequent environment (false) or commits which have been promoted (true).
    """
