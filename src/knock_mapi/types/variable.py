# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Variable"]


class Variable(BaseModel):
    """An environment variable object."""

    inserted_at: datetime
    """The timestamp of when the variable was created."""

    key: str
    """The key of the variable."""

    type: Literal["public", "secret"]
    """The type of the variable."""

    updated_at: datetime
    """The timestamp of when the variable was last updated."""

    value: str
    """The value of the variable."""

    description: Optional[str] = None
    """The description of the variable."""
