# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageTypeNumberField", "Settings"]


class Settings(TypedDict, total=False):
    """Settings for the number field."""

    default: Optional[float]
    """The default numeric value."""

    description: Optional[str]

    max: Optional[float]
    """Optional inclusive maximum allowed value."""

    min: Optional[float]
    """Optional inclusive minimum allowed value."""

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""

    unit_label: Optional[str]
    """Optional short label shown after the input (e.g. px, kg)."""


class MessageTypeNumberField(TypedDict, total=False):
    """
    A numeric field used in a message type or partial input schema, with optional min/max bounds and a unit label for display.
    """

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["number"]]
    """The type of the field."""

    settings: Settings
    """Settings for the number field."""
