# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageTypeListField", "Settings"]


class Settings(BaseModel):
    """Settings for the list field."""

    default: Optional[List[object]] = None
    """The default value of the list field."""

    description: Optional[str] = None

    item_schema: Optional[object] = None
    """A JSON schema used to validate the structure of each item in the list.

    Must be a valid JSON schema.
    """

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class MessageTypeListField(BaseModel):
    """A list field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["list"]
    """The type of the field."""

    settings: Optional[Settings] = None
    """Settings for the list field."""
