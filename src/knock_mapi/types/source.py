# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .source_environment_settings import SourceEnvironmentSettings

__all__ = ["Source"]


class Source(BaseModel):
    """A source that receives external events and maps them to Knock actions."""

    created_at: datetime
    """The timestamp of when the source was created."""

    environment_settings: Dict[str, SourceEnvironmentSettings]
    """Per-environment settings keyed by environment slug."""

    key: str
    """The unique key for the source within the project."""

    name: str
    """The human-readable name of the source."""

    updated_at: datetime
    """The timestamp of when the source was last updated."""

    custom_image_url: Optional[str] = None
    """An optional URL for a custom image representing the source."""

    description: Optional[str] = None
    """An optional description of the source."""
