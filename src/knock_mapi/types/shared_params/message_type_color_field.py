# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageTypeColorField", "Settings"]


class Settings(TypedDict, total=False):
    """Settings for the color field."""

    default: Optional[str]
    """The default hex color value."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class MessageTypeColorField(TypedDict, total=False):
    """
    A hex color field (#RGB or #RRGGBB) used in a message type or partial input schema.
    """

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["color"]]
    """The type of the field."""

    settings: Settings
    """Settings for the color field."""
