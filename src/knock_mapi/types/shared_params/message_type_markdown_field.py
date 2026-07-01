# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageTypeMarkdownField", "Settings"]


class Settings(TypedDict, total=False):
    """Settings for the markdown field."""

    default: str
    """The default value of the markdown field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class MessageTypeMarkdownField(TypedDict, total=False):
    """A markdown field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["markdown"]]
    """The type of the field."""

    settings: Settings
    """Settings for the markdown field."""
