# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .message_type_url_field import MessageTypeURLField
from ..message_type_text_field import MessageTypeTextField

__all__ = ["MessageTypeImageField", "Settings"]


class Settings(BaseModel):
    """Settings for the image field."""

    description: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeImageField(BaseModel):
    """An image field used in a message type."""

    action: MessageTypeTextField
    """A text field used in a message type."""

    alt: MessageTypeTextField
    """A text field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["image"]
    """The type of the field."""

    url: MessageTypeURLField
    """A URL field used in a message type."""

    settings: Optional[Settings] = None
    """Settings for the image field."""
