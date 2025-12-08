# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .message_type_variant import MessageTypeVariant

__all__ = ["MessageType"]


class MessageType(BaseModel):
    """
    A message type is a schema for a message that maps to a UI component or element within your application.
    """

    created_at: datetime
    """The timestamp of when the message type was created."""

    environment: str
    """The environment of the message type."""

    key: str
    """The unique key string for the message type object.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    name: str
    """A name for the message type. Must be at maximum 255 characters in length."""

    owner: Literal["system", "user"]
    """The owner of the message type."""

    preview: str
    """An HTML/liquid template for the message type preview."""

    semver: str
    """The semantic version of the message type."""

    sha: str
    """The SHA hash of the message type."""

    updated_at: datetime
    """The timestamp of when the message type was last updated."""

    valid: bool
    """Whether the message type is valid."""

    variants: List[MessageTypeVariant]
    """The variants of the message type."""

    archived_at: Optional[datetime] = None
    """The timestamp of when the message type was deleted."""

    deleted_at: Optional[datetime] = None
    """The timestamp of when the message type was deleted."""

    description: Optional[str] = None
    """An arbitrary string attached to a message type object.

    Useful for adding notes about the message type for internal purposes. Maximum of
    280 characters allowed.
    """

    icon_name: Optional[str] = None
    """The icon name of the message type."""
