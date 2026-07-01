# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..message_type_text_field_param import MessageTypeTextFieldParam

__all__ = ["MessageTypeButtonField", "Settings"]


class Settings(TypedDict, total=False):
    """Settings for the button field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class MessageTypeButtonField(TypedDict, total=False):
    """A button field used in a message type."""

    action: Required[MessageTypeTextFieldParam]
    """A text field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    text: Required[MessageTypeTextFieldParam]
    """A text field used in a message type."""

    type: Required[Literal["button"]]
    """The type of the field."""

    settings: Settings
    """Settings for the button field."""
