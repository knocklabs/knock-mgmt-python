# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageTypeJsonField", "Settings"]


class Settings(TypedDict, total=False):
    """Settings for the json field."""

    default: Optional[object]
    """The default value of the JSON field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""

    schema: Optional[object]
    """A JSON schema used to validate the structure of the JSON provided.

    Must be a valid JSON schema.
    """


class MessageTypeJsonField(TypedDict, total=False):
    """A JSON field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["json"]]
    """The type of the field."""

    settings: Settings
    """Settings for the json field."""
