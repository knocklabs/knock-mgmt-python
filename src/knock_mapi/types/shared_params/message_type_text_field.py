# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageTypeTextField", "Settings"]


class Settings(TypedDict, total=False):
    """Settings for the text field."""

    default: Optional[str]
    """The default value of the text field."""

    description: Optional[str]

    max_length: int

    min_length: int

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class MessageTypeTextField(TypedDict, total=False):
    """A text field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["text"]]
    """The type of the field."""

    settings: Settings
    """Settings for the text field."""
