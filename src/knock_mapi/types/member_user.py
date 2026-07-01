# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MemberUser"]


class MemberUser(BaseModel):
    """Information about a user within the Knock dashboard.

    Not to be confused with an external user (recipient) of a workflow.
    """

    id: str
    """The user's unique identifier."""

    created_at: datetime
    """The timestamp of when the user was created."""

    email: str
    """The user's email address."""

    updated_at: datetime
    """The timestamp of when the user was last updated."""

    avatar_url: Optional[str] = None
    """The URL of the user's avatar image."""

    name: Optional[str] = None
    """The user's display name."""
