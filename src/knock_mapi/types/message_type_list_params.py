# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageTypeListParams"]


class MessageTypeListParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    after: str
    """The cursor to fetch entries after."""

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    before: str
    """The cursor to fetch entries before."""

    hide_uncommitted_changes: bool
    """Whether to hide uncommitted changes.

    When true, only committed changes will be returned. When false, both committed
    and uncommitted changes will be returned.
    """

    limit: int
    """The number of entries to fetch per-page."""
