# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.page_info import PageInfo

__all__ = ["WarehouseSyncRetrieveRunsResponse", "Entry", "EntryError"]


class EntryError(BaseModel):
    """Why the run failed."""

    message: Optional[str] = None
    """What went wrong."""

    stage: Optional[Literal["extract", "load", "apply"]] = None
    """Where the run failed."""


class Entry(BaseModel):
    """
    One run of a warehouse sync: reading changed rows from the warehouse, then applying them in Knock.
    """

    id: str
    """The ID of the run."""

    status: Literal["running", "completed", "completed_with_errors", "failed"]
    """The status of the run."""

    ended_at: Optional[datetime] = None
    """When the run ended."""

    error: Optional[EntryError] = None
    """Why the run failed."""

    load_id: Optional[str] = None
    """The ID of the delivery of rows to Knock.

    Null when the run hasn't sent rows yet, failed before sending them, or found no
    changes.
    """

    records_errored: Optional[int] = None
    """How many rows failed before reaching Knock."""

    records_processed: Optional[int] = None
    """How many changed rows were read from the warehouse."""

    rows_applied: Optional[int] = None
    """How many rows were applied in Knock."""

    rows_failed: Optional[int] = None
    """How many rows failed to apply in Knock."""

    started_at: Optional[datetime] = None
    """When the run started."""

    submitted_at: Optional[datetime] = None
    """When the run was queued."""


class WarehouseSyncRetrieveRunsResponse(BaseModel):
    """A paginated list of WarehouseSyncRun.

    Contains a list of entries and page information.
    """

    entries: List[Entry]
    """A list of entries."""

    page_info: PageInfo
    """The information about a paginated result."""
