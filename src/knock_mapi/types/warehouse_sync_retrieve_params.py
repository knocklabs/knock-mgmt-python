# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WarehouseSyncRetrieveParams"]


class WarehouseSyncRetrieveParams(TypedDict, total=False):
    environment: str
    """The environment slug. When omitted, the account's default environment is used."""

    hide_uncommitted_changes: bool
    """Whether to hide uncommitted changes.

    When true, only committed changes will be returned. When false, both committed
    and uncommitted changes will be returned.
    """
