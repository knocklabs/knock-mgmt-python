# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    """A named tag in a project's resource-tag catalog."""

    created_at: datetime
    """The timestamp of when the tag was created."""

    name: str
    """The unique name of the tag within a project."""

    updated_at: datetime
    """The timestamp of when the tag was last updated."""

    color: Optional[str] = None
    """An optional hex color for the tag (e.g. #3B82F6)."""

    description: Optional[str] = None
    """An optional description of the tag."""
