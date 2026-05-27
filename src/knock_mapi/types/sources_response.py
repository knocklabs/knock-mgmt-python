# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SourcesResponse", "Entry"]


class Entry(BaseModel):
    """A source summary."""

    key: str
    """Source key."""

    name: str
    """Source display name."""

    custom_image_url: Optional[str] = None
    """Custom image URL for the source."""

    description: Optional[str] = None
    """Source description."""


class SourcesResponse(BaseModel):
    """Sources connected to the project."""

    entries: List[Entry]
    """Sources."""
