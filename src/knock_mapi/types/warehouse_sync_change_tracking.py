# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WarehouseSyncChangeTracking"]


class WarehouseSyncChangeTracking(BaseModel):
    """How the sync detects changed and deleted rows."""

    is_deleted_column: Optional[str] = None
    """A boolean column that marks a row as deleted. Requires `last_modified_column`."""

    last_modified_column: Optional[str] = None
    """A timestamp column that changes whenever a row changes.

    With it, each run reads only rows changed since the last run.
    """
