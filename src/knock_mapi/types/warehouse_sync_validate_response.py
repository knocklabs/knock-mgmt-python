# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .warehouse_sync_request import WarehouseSyncRequest

__all__ = ["WarehouseSyncValidateResponse"]


class WarehouseSyncValidateResponse(BaseModel):
    """Wraps the WarehouseSyncRequest response under the `warehouse_sync` key."""

    warehouse_sync: WarehouseSyncRequest
    """A warehouse sync payload for upsert or validate.

    Fields left out keep their current values. `warehouse_key`, `target_type`, and
    `target` are required to create a sync and can't change after. Change `enabled`
    and `frequency_minutes` with the settings endpoint.
    """
