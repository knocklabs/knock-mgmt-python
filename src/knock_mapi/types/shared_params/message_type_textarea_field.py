# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageTypeTextareaField", "Settings"]


class Settings(TypedDict, total=False):
    """Settings for the textarea field."""

    default: Optional[str]
    """The default value of the textarea field."""

    description: Optional[str]

    max_length: int

    min_length: int

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class MessageTypeTextareaField(TypedDict, total=False):
    """A textarea field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["textarea"]]
    """The type of the field."""

    settings: Settings
    """Settings for the textarea field."""
