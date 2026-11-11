# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WarehouseSyncTarget"]


class WarehouseSyncTarget(BaseModel):
    """The collection or audience the sync writes to.

    `object` and `subscription` syncs set `collection`, and `static_audience_membership` syncs set `audience_key`. Null for `user` and `tenant` syncs.
    """

    audience_key: Optional[str] = None
    """The key of the static audience the rows become members of."""

    collection: Optional[str] = None
    """The object collection the rows are written to."""
