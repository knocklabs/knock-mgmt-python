# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Asset"]


class Asset(BaseModel):
    """An uploaded asset file for an account."""

    id: str
    """The unique ID for this asset."""

    asset_type: str
    """The type of asset."""

    created_at: datetime
    """The timestamp of when this asset was created."""

    mime_type: str
    """The MIME type for this asset."""

    updated_at: datetime
    """The timestamp of when this asset was last updated."""

    url: str
    """The public URL for this asset."""

    filename: Optional[str] = None
    """The human-readable filename for this asset."""
