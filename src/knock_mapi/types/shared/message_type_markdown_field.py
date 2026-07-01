# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageTypeMarkdownField", "Settings"]


class Settings(BaseModel):
    """Settings for the markdown field."""

    default: Optional[str] = None
    """The default value of the markdown field."""

    description: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeMarkdownField(BaseModel):
    """A markdown field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["markdown"]
    """The type of the field."""

    settings: Optional[Settings] = None
    """Settings for the markdown field."""
