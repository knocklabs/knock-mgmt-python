# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .message_type_text_field_param import MessageTypeTextFieldParam

__all__ = [
    "MessageTypeVariantParam",
    "Field",
    "FieldMessageTypeBooleanField",
    "FieldMessageTypeBooleanFieldSettings",
    "FieldMessageTypeButtonField",
    "FieldMessageTypeButtonFieldSettings",
    "FieldMessageTypeImageField",
    "FieldMessageTypeImageFieldURL",
    "FieldMessageTypeImageFieldURLSettings",
    "FieldMessageTypeImageFieldSettings",
    "FieldMessageTypeJsonField",
    "FieldMessageTypeJsonFieldSettings",
    "FieldMessageTypeMarkdownField",
    "FieldMessageTypeMarkdownFieldSettings",
    "FieldMessageTypeMultiSelectField",
    "FieldMessageTypeMultiSelectFieldSettings",
    "FieldMessageTypeMultiSelectFieldSettingsOption",
    "FieldMessageTypeSelectField",
    "FieldMessageTypeSelectFieldSettings",
    "FieldMessageTypeSelectFieldSettingsOption",
    "FieldMessageTypeTextareaField",
    "FieldMessageTypeTextareaFieldSettings",
    "FieldMessageTypeURLField",
    "FieldMessageTypeURLFieldSettings",
]


class FieldMessageTypeBooleanFieldSettings(TypedDict, total=False):
    """Settings for the boolean field."""

    default: bool
    """The default value of the boolean field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeBooleanField(TypedDict, total=False):
    """A boolean field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["boolean"]]
    """The type of the field."""

    settings: FieldMessageTypeBooleanFieldSettings
    """Settings for the boolean field."""


class FieldMessageTypeButtonFieldSettings(TypedDict, total=False):
    """Settings for the button field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeButtonField(TypedDict, total=False):
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

    settings: FieldMessageTypeButtonFieldSettings
    """Settings for the button field."""


class FieldMessageTypeImageFieldURLSettings(TypedDict, total=False):
    """Settings for the url field."""

    default: Optional[str]
    """The default value of the URL field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeImageFieldURL(TypedDict, total=False):
    """A URL field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["url"]]
    """The type of the field."""

    settings: FieldMessageTypeImageFieldURLSettings
    """Settings for the url field."""


class FieldMessageTypeImageFieldSettings(TypedDict, total=False):
    """Settings for the image field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeImageField(TypedDict, total=False):
    """An image field used in a message type."""

    action: Required[MessageTypeTextFieldParam]
    """A text field used in a message type."""

    alt: Required[MessageTypeTextFieldParam]
    """A text field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["image"]]
    """The type of the field."""

    url: Required[FieldMessageTypeImageFieldURL]
    """A URL field used in a message type."""

    settings: FieldMessageTypeImageFieldSettings
    """Settings for the image field."""


class FieldMessageTypeJsonFieldSettings(TypedDict, total=False):
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


class FieldMessageTypeJsonField(TypedDict, total=False):
    """A JSON field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["json"]]
    """The type of the field."""

    settings: FieldMessageTypeJsonFieldSettings
    """Settings for the json field."""


class FieldMessageTypeMarkdownFieldSettings(TypedDict, total=False):
    """Settings for the markdown field."""

    default: str
    """The default value of the markdown field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeMarkdownField(TypedDict, total=False):
    """A markdown field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["markdown"]]
    """The type of the field."""

    settings: FieldMessageTypeMarkdownFieldSettings
    """Settings for the markdown field."""


class FieldMessageTypeMultiSelectFieldSettingsOption(TypedDict, total=False):
    value: Required[str]
    """The value for the option."""

    label: str
    """The display label for the option."""


class FieldMessageTypeMultiSelectFieldSettings(TypedDict, total=False):
    """Settings for the multi_select field."""

    default: Optional[SequenceNotStr[str]]
    """The default values for the multi-select field."""

    description: Optional[str]

    options: Iterable[FieldMessageTypeMultiSelectFieldSettingsOption]
    """The available options for the multi-select field."""

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeMultiSelectField(TypedDict, total=False):
    """A multi-select field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    settings: Required[FieldMessageTypeMultiSelectFieldSettings]
    """Settings for the multi_select field."""

    type: Required[Literal["multi_select"]]
    """The type of the field."""


class FieldMessageTypeSelectFieldSettingsOption(TypedDict, total=False):
    value: Required[str]
    """The value for the option."""

    label: str
    """The display label for the option."""


class FieldMessageTypeSelectFieldSettings(TypedDict, total=False):
    """Settings for the select field."""

    default: Optional[str]
    """The default value for the select field."""

    description: Optional[str]

    options: Iterable[FieldMessageTypeSelectFieldSettingsOption]
    """The available options for the select field."""

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeSelectField(TypedDict, total=False):
    """A select field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    settings: Required[FieldMessageTypeSelectFieldSettings]
    """Settings for the select field."""

    type: Required[Literal["select"]]
    """The type of the field."""


class FieldMessageTypeTextareaFieldSettings(TypedDict, total=False):
    """Settings for the textarea field."""

    default: Optional[str]
    """The default value of the textarea field."""

    description: Optional[str]

    max_length: int

    min_length: int

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeTextareaField(TypedDict, total=False):
    """A textarea field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["textarea"]]
    """The type of the field."""

    settings: FieldMessageTypeTextareaFieldSettings
    """Settings for the textarea field."""


class FieldMessageTypeURLFieldSettings(TypedDict, total=False):
    """Settings for the url field."""

    default: Optional[str]
    """The default value of the URL field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class FieldMessageTypeURLField(TypedDict, total=False):
    """A URL field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["url"]]
    """The type of the field."""

    settings: FieldMessageTypeURLFieldSettings
    """Settings for the url field."""


Field: TypeAlias = Union[
    FieldMessageTypeBooleanField,
    FieldMessageTypeButtonField,
    FieldMessageTypeImageField,
    FieldMessageTypeJsonField,
    FieldMessageTypeMarkdownField,
    FieldMessageTypeMultiSelectField,
    FieldMessageTypeSelectField,
    MessageTypeTextFieldParam,
    FieldMessageTypeTextareaField,
    FieldMessageTypeURLField,
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
