# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Branch"]


class Branch(BaseModel):
    created_at: datetime
    """The timestamp of when the branch was created."""

    slug: str
    """A unique slug for the branch. Cannot exceed 255 characters."""

    updated_at: datetime
    """The timestamp of when the branch was last updated."""

    deleted_at: Optional[datetime] = None
    """The timestamp of when the branch was deleted."""

    last_commit_at: Optional[datetime] = None
    """The timestamp of the most-recent commit in the branch."""
