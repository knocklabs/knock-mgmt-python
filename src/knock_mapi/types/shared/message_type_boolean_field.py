# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageTypeBooleanField", "Settings"]


class Settings(BaseModel):
    """Settings for the boolean field."""

    default: Optional[bool] = None
    """The default value of the boolean field."""

    description: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeBooleanField(BaseModel):
    """A boolean field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["boolean"]
    """The type of the field."""

    settings: Optional[Settings] = None
    """Settings for the boolean field."""
