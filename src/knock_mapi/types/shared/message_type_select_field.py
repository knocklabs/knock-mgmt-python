# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageTypeSelectField", "Settings", "SettingsOption"]


class SettingsOption(BaseModel):
    value: str
    """The value for the option."""

    label: Optional[str] = None
    """The display label for the option."""


class Settings(BaseModel):
    """Settings for the select field."""

    default: Optional[str] = None
    """The default value for the select field."""

    description: Optional[str] = None

    options: Optional[List[SettingsOption]] = None
    """The available options for the select field."""

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeSelectField(BaseModel):
    """A select field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    settings: Settings
    """Settings for the select field."""

    type: Literal["select"]
    """The type of the field."""
