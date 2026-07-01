# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .message_type_text_field_param import MessageTypeTextFieldParam
from .shared_params.message_type_url_field import MessageTypeURLField
from .shared_params.message_type_json_field import MessageTypeJsonField
from .shared_params.message_type_image_field import MessageTypeImageField
from .shared_params.message_type_button_field import MessageTypeButtonField
from .shared_params.message_type_select_field import MessageTypeSelectField
from .shared_params.message_type_boolean_field import MessageTypeBooleanField
from .shared_params.message_type_markdown_field import MessageTypeMarkdownField
from .shared_params.message_type_textarea_field import MessageTypeTextareaField
from .shared_params.message_type_multi_select_field import MessageTypeMultiSelectField

__all__ = [
    "PartialUpsertParams",
    "Partial",
    "PartialInputSchema",
    "PartialInputSchemaMessageTypeListField",
    "PartialInputSchemaMessageTypeListFieldSettings",
    "PartialInputSchemaMessageTypeNumberField",
    "PartialInputSchemaMessageTypeNumberFieldSettings",
    "PartialInputSchemaMessageTypeColorField",
    "PartialInputSchemaMessageTypeColorFieldSettings",
]


class PartialUpsertParams(TypedDict, total=False):
    environment: Required[str]
    """The environment slug."""

    partial: Required[Partial]
    """A partial object with attributes to update or create a partial."""

    annotate: bool
    """Whether to annotate the resource. Only used in the Knock CLI."""

    branch: str
    """The slug of a branch to use.

    This option can only be used when `environment` is `"development"`.
    """

    commit: bool
    """Whether to commit the resource at the same time as modifying it."""

    commit_message: str
    """The message to commit the resource with, only used if `commit` is `true`."""

    force: bool
    """
    When set to true, forces the upsert to override existing content regardless of
    environment restrictions. This bypasses the development-only environment check
    and origin environment checks.
    """


class PartialInputSchemaMessageTypeListFieldSettings(TypedDict, total=False):
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


class PartialInputSchemaMessageTypeListField(TypedDict, total=False):
    """A list field used in a message type."""

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["list"]]
    """The type of the field."""

    settings: PartialInputSchemaMessageTypeListFieldSettings
    """Settings for the list field."""


class PartialInputSchemaMessageTypeNumberFieldSettings(TypedDict, total=False):
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


class PartialInputSchemaMessageTypeNumberField(TypedDict, total=False):
    """
    A numeric field used in a message type or partial input schema, with optional min/max bounds and a unit label for display.
    """

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["number"]]
    """The type of the field."""

    settings: PartialInputSchemaMessageTypeNumberFieldSettings
    """Settings for the number field."""


class PartialInputSchemaMessageTypeColorFieldSettings(TypedDict, total=False):
    """Settings for the color field."""

    default: Optional[str]
    """The default hex color value."""

    description: Optional[str]

    placeholder: Optional[str]

    required: bool
    """Whether the field is required."""


class PartialInputSchemaMessageTypeColorField(TypedDict, total=False):
    """
    A hex color field (#RGB or #RRGGBB) used in a message type or partial input schema.
    """

    key: Required[str]
    """The unique key of the field."""

    label: Required[Optional[str]]
    """The label of the field."""

    type: Required[Literal["color"]]
    """The type of the field."""

    settings: PartialInputSchemaMessageTypeColorFieldSettings
    """Settings for the color field."""


PartialInputSchema: TypeAlias = Union[
    PartialInputSchemaMessageTypeListField,
    MessageTypeSelectField,
    MessageTypeBooleanField,
    MessageTypeJsonField,
    PartialInputSchemaMessageTypeNumberField,
    MessageTypeTextFieldParam,
    MessageTypeImageField,
    PartialInputSchemaMessageTypeColorField,
    MessageTypeURLField,
    MessageTypeMarkdownField,
    MessageTypeMultiSelectField,
    MessageTypeButtonField,
    MessageTypeTextareaField,
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
