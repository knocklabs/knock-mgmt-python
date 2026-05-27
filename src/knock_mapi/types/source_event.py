# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SourceEvent"]


class SourceEvent(BaseModel):
    """A known unique event received by a source."""

    event: str
    """The decoded event name."""

    last_received_at: Optional[datetime] = None
    """The timestamp of when this event was last received."""
