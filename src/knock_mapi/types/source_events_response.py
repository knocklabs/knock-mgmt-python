# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .source_event import SourceEvent

__all__ = ["SourceEventsResponse"]


class SourceEventsResponse(BaseModel):
    """A list of known unique source events."""

    entries: List[SourceEvent]
    """The known unique events for the requested source and environment."""
