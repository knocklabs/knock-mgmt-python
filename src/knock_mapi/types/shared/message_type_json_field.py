# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MessageTypeJsonField", "Settings"]


class Settings(BaseModel):
    """Settings for the json field."""

    default: Optional[object] = None
    """The default value of the JSON field."""

    description: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)
    """A JSON schema used to validate the structure of the JSON provided.

    Must be a valid JSON schema.
    """


class MessageTypeJsonField(BaseModel):
    """A JSON field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["json"]
    """The type of the field."""

    settings: Optional[Settings] = None
    """Settings for the json field."""
