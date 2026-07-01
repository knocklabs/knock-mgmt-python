# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MessageTypeMultiSelectField", "Settings", "SettingsOption"]


class SettingsOption(TypedDict, total=False):
    value: Required[str]
    """The value for the option."""

    label: str
    """The display label for the option."""


class Settings(TypedDict, total=False):
    """Settings for the multi_select field."""

    default: Optional[SequenceNotStr[str]]
    """The default values for the multi-select field."""

    description: Optional[str]

    options: Iterable[SettingsOption]
    """The available options for the multi-select field."""

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class MessageTypeMultiSelectField(TypedDict, total=False):
    """A multi-select field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    settings: Required[Settings]
    """Settings for the multi_select field."""

    type: Required[Literal["multi_select"]]
    """The type of the field."""
