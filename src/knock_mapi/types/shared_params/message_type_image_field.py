# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .message_type_url_field import MessageTypeURLField
from .message_type_text_field import MessageTypeTextField

__all__ = ["MessageTypeImageField", "Settings"]


class Settings(TypedDict, total=False):
    """Settings for the image field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class MessageTypeImageField(TypedDict, total=False):
    """An image field used in a message type."""

    action: Required[MessageTypeTextField]
    """A text field used in a message type."""

    alt: Required[MessageTypeTextField]
    """A text field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["image"]]
    """The type of the field."""

    url: Required[MessageTypeURLField]
    """A URL field used in a message type."""

    settings: Settings
    """Settings for the image field."""
