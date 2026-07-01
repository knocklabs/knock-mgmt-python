# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageTypeSelectField", "Settings", "SettingsOption"]


class SettingsOption(TypedDict, total=False):
    value: Required[str]
    """The value for the option."""

    label: str
    """The display label for the option."""


class Settings(TypedDict, total=False):
    """Settings for the select field."""

    default: Optional[str]
    """The default value for the select field."""

    description: Optional[str]

    options: Iterable[SettingsOption]
    """The available options for the select field."""

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class MessageTypeSelectField(TypedDict, total=False):
    """A select field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    settings: Required[Settings]
    """Settings for the select field."""

    type: Required[Literal["select"]]
    """The type of the field."""
