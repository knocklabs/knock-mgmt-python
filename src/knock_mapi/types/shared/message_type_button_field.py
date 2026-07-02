# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .message_type_text_field import MessageTypeTextField

__all__ = ["MessageTypeButtonField", "Settings"]


class Settings(BaseModel):
    """Settings for the button field."""

    description: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeButtonField(BaseModel):
    """A button field used in a message type."""

    action: MessageTypeTextField
    """A text field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    text: MessageTypeTextField
    """A text field used in a message type."""

    type: Literal["button"]
    """The type of the field."""

    settings: Optional[Settings] = None
    """Settings for the button field."""
