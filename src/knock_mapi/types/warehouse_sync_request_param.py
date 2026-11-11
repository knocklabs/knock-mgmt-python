# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .warehouse_sync_source_param import WarehouseSyncSourceParam
from .warehouse_sync_target_param import WarehouseSyncTargetParam
from .warehouse_sync_mapping_param import WarehouseSyncMappingParam
from .warehouse_sync_change_tracking_param import WarehouseSyncChangeTrackingParam

__all__ = ["WarehouseSyncRequestParam"]


class WarehouseSyncRequestParam(TypedDict, total=False):
    """A warehouse sync payload for upsert or validate.

    Fields left out keep their current values. `warehouse_key`, `target_type`, and `target` are required to create a sync and can't change after. Change `enabled` and `frequency_minutes` with the settings endpoint.
    """

    change_tracking: WarehouseSyncChangeTrackingParam
    """How the sync detects changed and deleted rows."""

    description: Optional[str]
    """An optional description of the sync. Maximum of 280 characters allowed."""

    mappings: Iterable[WarehouseSyncMappingParam]
    """How columns map to Knock fields."""

    name: str
    """The name of the sync.

    Must be at minimum 1 character and at maximum 255 characters in length.
    """

    primary_key_column: Optional[str]
    """The column that uniquely identifies each row."""

    source: WarehouseSyncSourceParam
    """
    The rows a warehouse sync reads: a table or view (`relation`), or the result of
    a SQL query (`sql`).
    """

    target: Optional[WarehouseSyncTargetParam]
    """The collection or audience the sync writes to.

    `object` and `subscription` syncs set `collection`, and
    `static_audience_membership` syncs set `audience_key`. Null for `user` and
    `tenant` syncs.
    """

    target_type: Literal["user", "tenant", "object", "static_audience_membership", "subscription"]
    """What each row becomes in Knock. Can't change after creation."""

    version_id: str
    """The `version_id` of the sync you last read.

    When it isn't the current version, someone saved since, and the request is
    refused.
    """

    warehouse_key: str
    """The key of the warehouse the sync reads from. Can't change after creation."""
