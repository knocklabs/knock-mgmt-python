# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["WarehouseSyncChangeTrackingParam"]


class WarehouseSyncChangeTrackingParam(TypedDict, total=False):
    """How the sync detects changed and deleted rows."""

    is_deleted_column: Optional[str]
    """A boolean column that marks a row as deleted. Requires `last_modified_column`."""

    last_modified_column: Optional[str]
    """A timestamp column that changes whenever a row changes.

    With it, each run reads only rows changed since the last run.
    """
