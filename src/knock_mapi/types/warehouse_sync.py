# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .warehouse_sync_source import WarehouseSyncSource
from .warehouse_sync_target import WarehouseSyncTarget
from .warehouse_sync_mapping import WarehouseSyncMapping
from .warehouse_sync_change_tracking import WarehouseSyncChangeTracking

__all__ = ["WarehouseSync", "LastFailure"]


class LastFailure(BaseModel):
    """The last run failure, cleared when a run succeeds."""

    message: Optional[str] = None
    """What went wrong."""

    stage: Optional[Literal["extract", "load", "apply"]] = None
    """
    Where the run failed: reading the warehouse (`extract`), sending rows to Knock
    (`load`), or applying them (`apply`).
    """


class WarehouseSync(BaseModel):
    """
    A warehouse sync reads rows from a warehouse on a schedule and writes them to Knock as users, tenants, objects, audience members, or subscriptions.
    """

    created_at: datetime
    """When the sync was created. (read-only)."""

    enabled: bool
    """Whether the sync runs on its schedule."""

    environment: str
    """The slug of the environment the sync belongs to. (read-only)."""

    frequency_minutes: Literal[10, 15, 60, 360, 720, 1440]
    """How often the sync runs, in minutes."""

    has_unpublished_changes: bool
    """Whether the sync has a draft that hasn't been published."""

    key: str
    """The unique key of the sync in its environment."""

    mappings: List[WarehouseSyncMapping]
    """How columns map to Knock fields."""

    name: str
    """The name of the sync.

    Must be at minimum 1 character and at maximum 255 characters in length.
    """

    sha: str
    """The SHA hash of the sync's definition. (read-only)."""

    status: Literal["draft", "publishing", "delivery_failed", "paused", "needs_attention", "live"]
    """The status of the sync."""

    target_type: Literal["user", "tenant", "object", "static_audience_membership", "subscription"]
    """What each row becomes in Knock. Can't change after creation."""

    updated_at: datetime
    """When the returned version was saved. (read-only)."""

    version_id: str
    """The ID of the version returned.

    Send it back when saving to make sure nobody saved since.
    """

    warehouse_key: str
    """The key of the warehouse the sync reads from. Can't change after creation."""

    change_tracking: Optional[WarehouseSyncChangeTracking] = None
    """How the sync detects changed and deleted rows."""

    description: Optional[str] = None
    """An optional description of the sync. Maximum of 280 characters allowed."""

    last_failure: Optional[LastFailure] = None
    """The last run failure, cleared when a run succeeds."""

    last_published_at: Optional[datetime] = None
    """When the sync was last published."""

    primary_key_column: Optional[str] = None
    """The column that uniquely identifies each row."""

    publish_error: Optional[str] = None
    """Why the last publish didn't go live, when it failed."""

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
