# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WarehouseSyncListParams"]


class WarehouseSyncListParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    hide_uncommitted_changes: bool
    """Whether to hide uncommitted changes.

    When true, only committed changes will be returned. When false, both committed
    and uncommitted changes will be returned.
    """

    limit: int
    """The number of entries to fetch per-page."""
