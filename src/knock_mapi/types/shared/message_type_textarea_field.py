# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageTypeTextareaField", "Settings"]


class Settings(BaseModel):
    """Settings for the textarea field."""

    default: Optional[str] = None
    """The default value of the textarea field."""

    description: Optional[str] = None

    max_length: Optional[int] = None

    min_length: Optional[int] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeTextareaField(BaseModel):
    """A textarea field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["textarea"]
    """The type of the field."""

    settings: Optional[Settings] = None
    """Settings for the textarea field."""
