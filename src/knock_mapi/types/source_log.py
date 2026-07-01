# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .source_log_action import SourceLogAction

__all__ = ["SourceLog"]


class SourceLog(BaseModel):
    """A log entry for an event received by a source."""

    id: str
    """The source log ID."""

    event: str
    """The decoded source event name."""

    actions: Optional[List[SourceLogAction]] = None
    """The actions executed after receiving the source event.

    Only present when `include` contains `actions`.
    """

    data: Optional[Dict[str, object]] = None
    """The data payload parsed by the source."""

    inserted_at: Optional[datetime] = None
    """The timestamp of when the source log was created."""

    preprocess_output: Optional[Dict[str, object]] = None
    """The output returned by the preprocess script."""

    source: Optional[str] = None
    """Indicates the origin of the log; if the log is a product of a test event.

    This is typically null for regular source events received from the data source.
    """

    verification_status: Optional[str] = None
    """The verification status for the received event."""
