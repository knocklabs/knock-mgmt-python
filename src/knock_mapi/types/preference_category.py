# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PreferenceCategory"]


class PreferenceCategory(BaseModel):
    """A named preference category in a project's catalog."""

    created_at: datetime
    """The timestamp of when the preference category was created."""

    name: str
    """The unique name of the preference category within a project."""

    updated_at: datetime
    """The timestamp of when the preference category was last updated."""

    archived_at: Optional[datetime] = None
    """The timestamp of when the preference category was archived."""
