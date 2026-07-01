# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .message_type_text_field import MessageTypeTextField
from .shared.message_type_url_field import MessageTypeURLField
from .shared.message_type_json_field import MessageTypeJsonField
from .shared.message_type_image_field import MessageTypeImageField
from .shared.message_type_button_field import MessageTypeButtonField
from .shared.message_type_select_field import MessageTypeSelectField
from .shared.message_type_boolean_field import MessageTypeBooleanField
from .shared.message_type_markdown_field import MessageTypeMarkdownField
from .shared.message_type_textarea_field import MessageTypeTextareaField
from .shared.message_type_multi_select_field import MessageTypeMultiSelectField

__all__ = [
    "Partial",
    "InputSchema",
    "InputSchemaMessageTypeListField",
    "InputSchemaMessageTypeListFieldSettings",
    "InputSchemaMessageTypeNumberField",
    "InputSchemaMessageTypeNumberFieldSettings",
    "InputSchemaMessageTypeColorField",
    "InputSchemaMessageTypeColorFieldSettings",
]


class InputSchemaMessageTypeListFieldSettings(BaseModel):
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


class InputSchemaMessageTypeListField(BaseModel):
    """A list field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["list"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeListFieldSettings] = None
    """Settings for the list field."""


class InputSchemaMessageTypeNumberFieldSettings(BaseModel):
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


class InputSchemaMessageTypeNumberField(BaseModel):
    """
    A numeric field used in a message type or partial input schema, with optional min/max bounds and a unit label for display.
    """

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["number"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeNumberFieldSettings] = None
    """Settings for the number field."""


class InputSchemaMessageTypeColorFieldSettings(BaseModel):
    """Settings for the color field."""

    default: Optional[str] = None
    """The default hex color value."""

    description: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeColorField(BaseModel):
    """
    A hex color field (#RGB or #RRGGBB) used in a message type or partial input schema.
    """

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["color"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeColorFieldSettings] = None
    """Settings for the color field."""


InputSchema: TypeAlias = Union[
    InputSchemaMessageTypeListField,
    MessageTypeSelectField,
    MessageTypeBooleanField,
    MessageTypeJsonField,
    InputSchemaMessageTypeNumberField,
    MessageTypeTextField,
    MessageTypeImageField,
    InputSchemaMessageTypeColorField,
    MessageTypeURLField,
    MessageTypeMarkdownField,
    MessageTypeMultiSelectField,
    MessageTypeButtonField,
    MessageTypeTextareaField,
]


class Partial(BaseModel):
    """A partial is a reusable piece of content that can be used in a template."""

    content: str
    """The partial content."""

    inserted_at: datetime
    """The timestamp of when the partial was created."""

    key: str
    """The unique key string for the partial object.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    name: str
    """A name for the partial. Must be at maximum 255 characters in length."""

    type: Literal["html", "text", "json", "markdown"]
    """The partial type. One of 'html', 'json', 'markdown', 'text'."""

    updated_at: datetime
    """The timestamp of when the partial was last updated."""

    valid: bool
    """Whether the partial and its content are in a valid state."""

    description: Optional[str] = None
    """An arbitrary string attached to a partial object.

    Useful for adding notes about the partial for internal purposes. Maximum of 280
    characters allowed.
    """

    environment: Optional[str] = None
    """The slug of the environment in which the partial exists."""

    icon_name: Optional[str] = None
    """The name of the icon to be used in the visual editor."""

    input_schema: Optional[List[InputSchema]] = None
    """The field types available for the partial."""

    visual_block_enabled: Optional[bool] = None
    """Indicates whether the partial can be used in the visual editor.

    Only applies to HTML partials.
    """
