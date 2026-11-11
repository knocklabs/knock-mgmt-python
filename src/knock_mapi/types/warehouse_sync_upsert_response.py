# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .warehouse_sync import WarehouseSync

__all__ = ["WarehouseSyncUpsertResponse"]


class WarehouseSyncUpsertResponse(BaseModel):
    """Wraps the WarehouseSync response under the `warehouse_sync` key."""

    warehouse_sync: WarehouseSync
    """
    A warehouse sync reads rows from a warehouse on a schedule and writes them to
    Knock as users, tenants, objects, audience members, or subscriptions.
    """
