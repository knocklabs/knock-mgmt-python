# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageTypeColorField", "Settings"]


class Settings(BaseModel):
    """Settings for the color field."""

    default: Optional[str] = None
    """The default hex color value."""

    description: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeColorField(BaseModel):
    """
    A hex color field (#RGB or #RRGGBB) used in a message type or partial input schema.
    """

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["color"]
    """The type of the field."""

    settings: Optional[Settings] = None
    """Settings for the color field."""
