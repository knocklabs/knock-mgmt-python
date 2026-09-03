# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageTypeNumberField", "Settings"]


class Settings(BaseModel):
    """Settings for the number field."""

    default: Optional[float] = None
    """The default numeric value."""

    description: Optional[str] = None

    max: Optional[float] = None
    """Optional inclusive maximum allowed value."""

    min: Optional[float] = None
    """Optional inclusive minimum allowed value."""

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""

    unit_label: Optional[str] = None
    """Optional short label shown after the input (e.g. px, kg)."""


class MessageTypeNumberField(BaseModel):
    """
    A numeric field used in a message type or partial input schema, with optional min/max bounds and a unit label for display.
    """

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["number"]
    """The type of the field."""

    settings: Optional[Settings] = None
    """Settings for the number field."""
