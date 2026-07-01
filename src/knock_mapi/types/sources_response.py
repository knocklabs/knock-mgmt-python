# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .source_environment_settings import SourceEnvironmentSettings

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

    environment_settings: Optional[Dict[str, SourceEnvironmentSettings]] = None
    """Per-environment settings keyed by environment slug.

    Present only when requested via `include`.
    """


class SourcesResponse(BaseModel):
    """Sources connected to the project."""

    entries: List[Entry]
    """Sources."""
