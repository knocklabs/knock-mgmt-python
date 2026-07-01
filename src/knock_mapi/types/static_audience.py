# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StaticAudience"]


class StaticAudience(BaseModel):
    """A static audience where members are explicitly added or removed via the API."""

    created_at: datetime
    """The timestamp of when the audience was created."""

    environment: str
    """The slug of the environment in which the audience exists."""

    key: str
    """The unique key of the audience."""

    name: str
    """The name of the audience."""

    type: Literal["static"]
    """The type of audience. Always `static` for static audiences."""

    updated_at: datetime
    """The timestamp of when the audience was last updated."""

    description: Optional[str] = None
    """A description of the audience."""

    sha: Optional[str] = None
    """The SHA hash of the audience data."""
