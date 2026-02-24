# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .message_type_text_field_param import MessageTypeTextFieldParam

__all__ = [
    "PartialValidateParams",
    "Partial",
    "PartialInputSchema",
    "PartialInputSchemaMessageTypeBooleanField",
    "PartialInputSchemaMessageTypeBooleanFieldSettings",
    "PartialInputSchemaMessageTypeButtonField",
    "PartialInputSchemaMessageTypeButtonFieldSettings",
    "PartialInputSchemaMessageTypeImageField",
    "PartialInputSchemaMessageTypeImageFieldURL",
    "PartialInputSchemaMessageTypeImageFieldURLSettings",
    "PartialInputSchemaMessageTypeImageFieldSettings",
    "PartialInputSchemaMessageTypeJsonField",
    "PartialInputSchemaMessageTypeJsonFieldSettings",
    "PartialInputSchemaMessageTypeMarkdownField",
    "PartialInputSchemaMessageTypeMarkdownFieldSettings",
    "PartialInputSchemaMessageTypeMultiSelectField",
    "PartialInputSchemaMessageTypeMultiSelectFieldSettings",
    "PartialInputSchemaMessageTypeMultiSelectFieldSettingsOption",
    "PartialInputSchemaMessageTypeSelectField",
    "PartialInputSchemaMessageTypeSelectFieldSettings",
    "PartialInputSchemaMessageTypeSelectFieldSettingsOption",
    "PartialInputSchemaMessageTypeTextareaField",
    "PartialInputSchemaMessageTypeTextareaFieldSettings",
    "PartialInputSchemaMessageTypeURLField",
    "PartialInputSchemaMessageTypeURLFieldSettings",
]


class PartialValidateParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    partial: Required[Partial]
    """A partial object with attributes to update or create a partial."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """


class PartialInputSchemaMessageTypeBooleanFieldSettings(TypedDict, total=False):
    """Settings for the boolean field."""

    default: bool
    """The default value of the boolean field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeBooleanField(TypedDict, total=False):
    """A boolean field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["boolean"]]
    """The type of the field."""

    settings: PartialInputSchemaMessageTypeBooleanFieldSettings
    """Settings for the boolean field."""


class PartialInputSchemaMessageTypeButtonFieldSettings(TypedDict, total=False):
    """Settings for the button field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeButtonField(TypedDict, total=False):
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

    settings: PartialInputSchemaMessageTypeButtonFieldSettings
    """Settings for the button field."""


class PartialInputSchemaMessageTypeImageFieldURLSettings(TypedDict, total=False):
    """Settings for the url field."""

    default: Optional[str]
    """The default value of the URL field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeImageFieldURL(TypedDict, total=False):
    """A URL field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["url"]]
    """The type of the field."""

    settings: PartialInputSchemaMessageTypeImageFieldURLSettings
    """Settings for the url field."""


class PartialInputSchemaMessageTypeImageFieldSettings(TypedDict, total=False):
    """Settings for the image field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeImageField(TypedDict, total=False):
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

    url: Required[PartialInputSchemaMessageTypeImageFieldURL]
    """A URL field used in a message type."""

    settings: PartialInputSchemaMessageTypeImageFieldSettings
    """Settings for the image field."""


class PartialInputSchemaMessageTypeJsonFieldSettings(TypedDict, total=False):
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


class PartialInputSchemaMessageTypeJsonField(TypedDict, total=False):
    """A JSON field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["json"]]
    """The type of the field."""

    settings: PartialInputSchemaMessageTypeJsonFieldSettings
    """Settings for the json field."""


class PartialInputSchemaMessageTypeMarkdownFieldSettings(TypedDict, total=False):
    """Settings for the markdown field."""

    default: str
    """The default value of the markdown field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeMarkdownField(TypedDict, total=False):
    """A markdown field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["markdown"]]
    """The type of the field."""

    settings: PartialInputSchemaMessageTypeMarkdownFieldSettings
    """Settings for the markdown field."""


class PartialInputSchemaMessageTypeMultiSelectFieldSettingsOption(TypedDict, total=False):
    value: Required[str]
    """The value for the option."""

    label: str
    """The display label for the option."""


class PartialInputSchemaMessageTypeMultiSelectFieldSettings(TypedDict, total=False):
    """Settings for the multi_select field."""

    default: Optional[SequenceNotStr[str]]
    """The default values for the multi-select field."""

    description: Optional[str]

    options: Iterable[PartialInputSchemaMessageTypeMultiSelectFieldSettingsOption]
    """The available options for the multi-select field."""

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeMultiSelectField(TypedDict, total=False):
    """A multi-select field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    settings: Required[PartialInputSchemaMessageTypeMultiSelectFieldSettings]
    """Settings for the multi_select field."""

    type: Required[Literal["multi_select"]]
    """The type of the field."""


class PartialInputSchemaMessageTypeSelectFieldSettingsOption(TypedDict, total=False):
    value: Required[str]
    """The value for the option."""

    label: str
    """The display label for the option."""


class PartialInputSchemaMessageTypeSelectFieldSettings(TypedDict, total=False):
    """Settings for the select field."""

    default: Optional[str]
    """The default value for the select field."""

    description: Optional[str]

    options: Iterable[PartialInputSchemaMessageTypeSelectFieldSettingsOption]
    """The available options for the select field."""

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeSelectField(TypedDict, total=False):
    """A select field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    settings: Required[PartialInputSchemaMessageTypeSelectFieldSettings]
    """Settings for the select field."""

    type: Required[Literal["select"]]
    """The type of the field."""


class PartialInputSchemaMessageTypeTextareaFieldSettings(TypedDict, total=False):
    """Settings for the textarea field."""

    default: Optional[str]
    """The default value of the textarea field."""

    description: Optional[str]

    max_length: int

    min_length: int

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeTextareaField(TypedDict, total=False):
    """A textarea field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["textarea"]]
    """The type of the field."""

    settings: PartialInputSchemaMessageTypeTextareaFieldSettings
    """Settings for the textarea field."""


class PartialInputSchemaMessageTypeURLFieldSettings(TypedDict, total=False):
    """Settings for the url field."""

    default: Optional[str]
    """The default value of the URL field."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeURLField(TypedDict, total=False):
    """A URL field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["url"]]
    """The type of the field."""

    settings: PartialInputSchemaMessageTypeURLFieldSettings
    """Settings for the url field."""


PartialInputSchema: TypeAlias = Union[
    PartialInputSchemaMessageTypeBooleanField,
    PartialInputSchemaMessageTypeButtonField,
    PartialInputSchemaMessageTypeImageField,
    PartialInputSchemaMessageTypeJsonField,
    PartialInputSchemaMessageTypeMarkdownField,
    PartialInputSchemaMessageTypeMultiSelectField,
    PartialInputSchemaMessageTypeSelectField,
    MessageTypeTextFieldParam,
    PartialInputSchemaMessageTypeTextareaField,
    PartialInputSchemaMessageTypeURLField,
]


class Partial(TypedDict, total=False):
    """A partial object with attributes to update or create a partial."""

    content: Required[str]
    """The partial content."""

    name: Required[str]
    """A name for the partial. Must be at maximum 255 characters in length."""

    type: Required[Literal["html", "text", "json", "markdown"]]
    """The partial type. One of 'html', 'json', 'markdown', 'text'."""

    description: str
    """An arbitrary string attached to a partial object.

    Useful for adding notes about the partial for internal purposes. Maximum of 280
    characters allowed.
    """

    icon_name: str
    """The name of the icon to be used in the visual editor."""

    input_schema: Iterable[PartialInputSchema]
    """The field types available for the partial."""

    visual_block_enabled: bool
    """Indicates whether the partial can be used in the visual editor.

    Only applies to HTML partials.
    """
