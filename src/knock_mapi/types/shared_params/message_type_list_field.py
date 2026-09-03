# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageTypeListField", "Settings"]


class Settings(TypedDict, total=False):
    """Settings for the list field."""

    default: Optional[Iterable[object]]
    """The default value of the list field."""

    description: Optional[str]

    item_schema: Optional[object]
    """A JSON schema used to validate the structure of each item in the list.

    Must be a valid JSON schema.
    """

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class MessageTypeListField(TypedDict, total=False):
    """A list field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["list"]]
    """The type of the field."""

    settings: Settings
    """Settings for the list field."""
