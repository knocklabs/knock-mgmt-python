# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageTypeMultiSelectField", "Settings", "SettingsOption"]


class SettingsOption(BaseModel):
    value: str
    """The value for the option."""

    label: Optional[str] = None
    """The display label for the option."""


class Settings(BaseModel):
    """Settings for the multi_select field."""

    default: Optional[List[str]] = None
    """The default values for the multi-select field."""

    description: Optional[str] = None

    options: Optional[List[SettingsOption]] = None
    """The available options for the multi-select field."""

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeMultiSelectField(BaseModel):
    """A multi-select field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    settings: Settings
    """Settings for the multi_select field."""

    type: Literal["multi_select"]
    """The type of the field."""
