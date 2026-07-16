# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.message_type_url_field import MessageTypeURLField
from .shared_params.message_type_json_field import MessageTypeJsonField
from .shared_params.message_type_text_field import MessageTypeTextField
from .shared_params.message_type_image_field import MessageTypeImageField
from .shared_params.message_type_button_field import MessageTypeButtonField
from .shared_params.message_type_select_field import MessageTypeSelectField
from .shared_params.message_type_boolean_field import MessageTypeBooleanField
from .shared_params.message_type_markdown_field import MessageTypeMarkdownField
from .shared_params.message_type_textarea_field import MessageTypeTextareaField
from .shared_params.message_type_multi_select_field import MessageTypeMultiSelectField

__all__ = [
    "MessageTypeVariantParam",
    "Field",
    "FieldMessageTypeListField",
    "FieldMessageTypeListFieldSettings",
    "FieldMessageTypeNumberField",
    "FieldMessageTypeNumberFieldSettings",
    "FieldMessageTypeColorField",
    "FieldMessageTypeColorFieldSettings",
]


class FieldMessageTypeListFieldSettings(TypedDict, total=False):
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


class FieldMessageTypeListField(TypedDict, total=False):
    """A list field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["list"]]
    """The type of the field."""

    settings: FieldMessageTypeListFieldSettings
    """Settings for the list field."""


class FieldMessageTypeNumberFieldSettings(TypedDict, total=False):
    """Settings for the number field."""

    default: Optional[float]
    """The default numeric value."""

    description: Optional[str]

    max: Optional[float]
    """Optional inclusive maximum allowed value."""

    min: Optional[float]
    """Optional inclusive minimum allowed value."""

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""

    unit_label: Optional[str]
    """Optional short label shown after the input (e.g. px, kg)."""


class FieldMessageTypeNumberField(TypedDict, total=False):
    """
    A numeric field used in a message type or partial input schema, with optional min/max bounds and a unit label for display.
    """

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["number"]]
    """The type of the field."""

    settings: FieldMessageTypeNumberFieldSettings
    """Settings for the number field."""


class FieldMessageTypeColorFieldSettings(TypedDict, total=False):
    """Settings for the color field."""

    default: Optional[str]
    """The default hex color value."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeColorField(TypedDict, total=False):
    """
    A hex color field (#RGB or #RRGGBB) used in a message type or partial input schema.
    """

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["color"]]
    """The type of the field."""

    settings: FieldMessageTypeColorFieldSettings
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


class MessageTypeVariantParam(TypedDict, total=False):
    """A variant of a message type."""

    fields: Required[Iterable[Field]]
    """The field types available for the variant."""

    key: Required[str]
    """The unique key string for the variant.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    name: Required[str]
    """A name for the variant. Must be at maximum 255 characters in length."""
