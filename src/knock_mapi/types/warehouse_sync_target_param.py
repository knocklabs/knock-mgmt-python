# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["WarehouseSyncTargetParam"]


class WarehouseSyncTargetParam(TypedDict, total=False):
    """The collection or audience the sync writes to.

    `object` and `subscription` syncs set `collection`, and `static_audience_membership` syncs set `audience_key`. Null for `user` and `tenant` syncs.
    """

    audience_key: Optional[str]
    """The key of the static audience the rows become members of."""

    collection: Optional[str]
    """The object collection the rows are written to."""
