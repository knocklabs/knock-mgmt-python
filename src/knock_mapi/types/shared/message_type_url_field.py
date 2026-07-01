# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageTypeURLField", "Settings"]


class Settings(BaseModel):
    """Settings for the url field."""

    default: Optional[str] = None
    """The default value of the URL field."""

    description: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeURLField(BaseModel):
    """A URL field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["url"]
    """The type of the field."""

    settings: Optional[Settings] = None
    """Settings for the url field."""
