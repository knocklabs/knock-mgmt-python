# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.message_type_url_field import MessageTypeURLField
from .shared.message_type_json_field import MessageTypeJsonField
from .shared.message_type_text_field import MessageTypeTextField
from .shared.message_type_image_field import MessageTypeImageField
from .shared.message_type_button_field import MessageTypeButtonField
from .shared.message_type_select_field import MessageTypeSelectField
from .shared.message_type_boolean_field import MessageTypeBooleanField
from .shared.message_type_markdown_field import MessageTypeMarkdownField
from .shared.message_type_textarea_field import MessageTypeTextareaField
from .shared.message_type_multi_select_field import MessageTypeMultiSelectField

__all__ = [
    "MessageTypeVariant",
    "Field",
    "FieldMessageTypeListField",
    "FieldMessageTypeListFieldSettings",
    "FieldMessageTypeNumberField",
    "FieldMessageTypeNumberFieldSettings",
    "FieldMessageTypeColorField",
    "FieldMessageTypeColorFieldSettings",
]


class FieldMessageTypeListFieldSettings(BaseModel):
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


class FieldMessageTypeListField(BaseModel):
    """A list field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["list"]
    """The type of the field."""

    settings: Optional[FieldMessageTypeListFieldSettings] = None
    """Settings for the list field."""


class FieldMessageTypeNumberFieldSettings(BaseModel):
    """Settings for the number field."""

    default: Optional[float] = None
    """The default numeric value."""

    description: Optional[str] = None

    max: Optional[float] = None
    """Optional inclusive maximum allowed value."""

    min: Optional[float] = None
    """Optional inclusive minimum allowed value."""

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""

    unit_label: Optional[str] = None
    """Optional short label shown after the input (e.g. px, kg)."""


class FieldMessageTypeNumberField(BaseModel):
    """
    A numeric field used in a message type or partial input schema, with optional min/max bounds and a unit label for display.
    """

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["number"]
    """The type of the field."""

    settings: Optional[FieldMessageTypeNumberFieldSettings] = None
    """Settings for the number field."""


class FieldMessageTypeColorFieldSettings(BaseModel):
    """Settings for the color field."""

    default: Optional[str] = None
    """The default hex color value."""

    description: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeColorField(BaseModel):
    """
    A hex color field (#RGB or #RRGGBB) used in a message type or partial input schema.
    """

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["color"]
    """The type of the field."""

    settings: Optional[FieldMessageTypeColorFieldSettings] = None
    """Settings for the color field."""


Field: TypeAlias = Union[
    FieldMessageTypeListField,
    MessageTypeSelectField,
    MessageTypeBooleanField,
    MessageTypeJsonField,
    MessageTypeTextField,
    FieldMessageTypeNumberField,
    MessageTypeImageField,
    FieldMessageTypeColorField,
    MessageTypeURLField,
    MessageTypeMarkdownField,
    MessageTypeMultiSelectField,
    MessageTypeButtonField,
    MessageTypeTextareaField,
]


class MessageTypeVariant(BaseModel):
    """A variant of a message type."""

    fields: List[Field]
    """The field types available for the variant."""

    key: str
    """The unique key string for the variant.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    name: str
    """A name for the variant. Must be at maximum 255 characters in length."""
