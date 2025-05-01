# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Partial"]


class Partial(BaseModel):
    content: str
    """The partial content."""

    inserted_at: datetime
    """The timestamp of when the partial was created."""

    key: str
    """The unique key string for the partial object.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    name: str
    """A name for the partial. Must be at maximum 255 characters in length."""

    type: Literal["html", "text", "json", "markdown"]
    """The partial type. One of 'html', 'json', 'markdown', 'text'."""

    updated_at: datetime
    """The timestamp of when the partial was last updated."""

    valid: bool
    """Whether the partial and its content are in a valid state."""

    description: Optional[str] = None
    """An arbitrary string attached to a partial object.

    Useful for adding notes about the partial for internal purposes. Maximum of 280
    characters allowed.
    """

    environment: Optional[str] = None
    """The slug of the environment in which the partial exists."""

    icon_name: Optional[str] = None
    """The name of the icon to be used in the visual editor."""

    visual_block_enabled: Optional[bool] = None
    """Indicates whether the partial can be used in the visual editor.

    Only applies to HTML partials.
    """
