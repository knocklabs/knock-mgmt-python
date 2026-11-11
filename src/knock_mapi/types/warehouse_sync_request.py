# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .warehouse_sync_source import WarehouseSyncSource
from .warehouse_sync_target import WarehouseSyncTarget
from .warehouse_sync_mapping import WarehouseSyncMapping
from .warehouse_sync_change_tracking import WarehouseSyncChangeTracking

__all__ = ["WarehouseSyncRequest"]


class WarehouseSyncRequest(BaseModel):
    """A warehouse sync payload for upsert or validate.

    Fields left out keep their current values. `warehouse_key`, `target_type`, and `target` are required to create a sync and can't change after. Change `enabled` and `frequency_minutes` with the settings endpoint.
    """

    change_tracking: Optional[WarehouseSyncChangeTracking] = None
    """How the sync detects changed and deleted rows."""

    description: Optional[str] = None
    """An optional description of the sync. Maximum of 280 characters allowed."""

    mappings: Optional[List[WarehouseSyncMapping]] = None
    """How columns map to Knock fields."""

    name: Optional[str] = None
    """The name of the sync.

    Must be at minimum 1 character and at maximum 255 characters in length.
    """

    primary_key_column: Optional[str] = None
    """The column that uniquely identifies each row."""

    source: Optional[WarehouseSyncSource] = None
    """
    The rows a warehouse sync reads: a table or view (`relation`), or the result of
    a SQL query (`sql`).
    """

    target: Optional[WarehouseSyncTarget] = None
    """The collection or audience the sync writes to.

    `object` and `subscription` syncs set `collection`, and
    `static_audience_membership` syncs set `audience_key`. Null for `user` and
    `tenant` syncs.
    """

    target_type: Optional[Literal["user", "tenant", "object", "static_audience_membership", "subscription"]] = None
    """What each row becomes in Knock. Can't change after creation."""

    version_id: Optional[str] = None
    """The `version_id` of the sync you last read.

    When it isn't the current version, someone saved since, and the request is
    refused.
    """

    warehouse_key: Optional[str] = None
    """The key of the warehouse the sync reads from. Can't change after creation."""
