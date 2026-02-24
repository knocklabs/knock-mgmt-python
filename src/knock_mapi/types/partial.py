# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .message_type_text_field import MessageTypeTextField

__all__ = [
    "Partial",
    "InputSchema",
    "InputSchemaMessageTypeBooleanField",
    "InputSchemaMessageTypeBooleanFieldSettings",
    "InputSchemaMessageTypeButtonField",
    "InputSchemaMessageTypeButtonFieldSettings",
    "InputSchemaMessageTypeImageField",
    "InputSchemaMessageTypeImageFieldURL",
    "InputSchemaMessageTypeImageFieldURLSettings",
    "InputSchemaMessageTypeImageFieldSettings",
    "InputSchemaMessageTypeJsonField",
    "InputSchemaMessageTypeJsonFieldSettings",
    "InputSchemaMessageTypeMarkdownField",
    "InputSchemaMessageTypeMarkdownFieldSettings",
    "InputSchemaMessageTypeMultiSelectField",
    "InputSchemaMessageTypeMultiSelectFieldSettings",
    "InputSchemaMessageTypeMultiSelectFieldSettingsOption",
    "InputSchemaMessageTypeSelectField",
    "InputSchemaMessageTypeSelectFieldSettings",
    "InputSchemaMessageTypeSelectFieldSettingsOption",
    "InputSchemaMessageTypeTextareaField",
    "InputSchemaMessageTypeTextareaFieldSettings",
    "InputSchemaMessageTypeURLField",
    "InputSchemaMessageTypeURLFieldSettings",
]


class InputSchemaMessageTypeBooleanFieldSettings(BaseModel):
    """Settings for the boolean field."""

    default: Optional[bool] = None
    """The default value of the boolean field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeBooleanField(BaseModel):
    """A boolean field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["boolean"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeBooleanFieldSettings] = None
    """Settings for the boolean field."""


class InputSchemaMessageTypeButtonFieldSettings(BaseModel):
    """Settings for the button field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeButtonField(BaseModel):
    """A button field used in a message type."""

    action: MessageTypeTextField
    """A text field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    text: MessageTypeTextField
    """A text field used in a message type."""

    type: Literal["button"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeButtonFieldSettings] = None
    """Settings for the button field."""


class InputSchemaMessageTypeImageFieldURLSettings(BaseModel):
    """Settings for the url field."""

    default: Optional[str] = None
    """The default value of the URL field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeImageFieldURL(BaseModel):
    """A URL field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["url"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeImageFieldURLSettings] = None
    """Settings for the url field."""


class InputSchemaMessageTypeImageFieldSettings(BaseModel):
    """Settings for the image field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeImageField(BaseModel):
    """An image field used in a message type."""

    action: MessageTypeTextField
    """A text field used in a message type."""

    alt: MessageTypeTextField
    """A text field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["image"]
    """The type of the field."""

    url: InputSchemaMessageTypeImageFieldURL
    """A URL field used in a message type."""

    settings: Optional[InputSchemaMessageTypeImageFieldSettings] = None
    """Settings for the image field."""


class InputSchemaMessageTypeJsonFieldSettings(BaseModel):
    """Settings for the json field."""

    default: Optional[object] = None
    """The default value of the JSON field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)
    """A JSON schema used to validate the structure of the JSON provided.

    Must be a valid JSON schema.
    """


class InputSchemaMessageTypeJsonField(BaseModel):
    """A JSON field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["json"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeJsonFieldSettings] = None
    """Settings for the json field."""


class InputSchemaMessageTypeMarkdownFieldSettings(BaseModel):
    """Settings for the markdown field."""

    default: Optional[str] = None
    """The default value of the markdown field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeMarkdownField(BaseModel):
    """A markdown field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["markdown"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeMarkdownFieldSettings] = None
    """Settings for the markdown field."""


class InputSchemaMessageTypeMultiSelectFieldSettingsOption(BaseModel):
    value: str
    """The value for the option."""

    label: Optional[str] = None
    """The display label for the option."""


class InputSchemaMessageTypeMultiSelectFieldSettings(BaseModel):
    """Settings for the multi_select field."""

    default: Optional[List[str]] = None
    """The default values for the multi-select field."""

    description: Optional[str] = None

    options: Optional[List[InputSchemaMessageTypeMultiSelectFieldSettingsOption]] = None
    """The available options for the multi-select field."""

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeMultiSelectField(BaseModel):
    """A multi-select field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    settings: InputSchemaMessageTypeMultiSelectFieldSettings
    """Settings for the multi_select field."""

    type: Literal["multi_select"]
    """The type of the field."""


class InputSchemaMessageTypeSelectFieldSettingsOption(BaseModel):
    value: str
    """The value for the option."""

    label: Optional[str] = None
    """The display label for the option."""


class InputSchemaMessageTypeSelectFieldSettings(BaseModel):
    """Settings for the select field."""

    default: Optional[str] = None
    """The default value for the select field."""

    description: Optional[str] = None

    options: Optional[List[InputSchemaMessageTypeSelectFieldSettingsOption]] = None
    """The available options for the select field."""

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeSelectField(BaseModel):
    """A select field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    settings: InputSchemaMessageTypeSelectFieldSettings
    """Settings for the select field."""

    type: Literal["select"]
    """The type of the field."""


class InputSchemaMessageTypeTextareaFieldSettings(BaseModel):
    """Settings for the textarea field."""

    default: Optional[str] = None
    """The default value of the textarea field."""

    description: Optional[str] = None

    max_length: Optional[int] = None

    min_length: Optional[int] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeTextareaField(BaseModel):
    """A textarea field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["textarea"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeTextareaFieldSettings] = None
    """Settings for the textarea field."""


class InputSchemaMessageTypeURLFieldSettings(BaseModel):
    """Settings for the url field."""

    default: Optional[str] = None
    """The default value of the URL field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class InputSchemaMessageTypeURLField(BaseModel):
    """A URL field used in a message type."""

    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["url"]
    """The type of the field."""

    settings: Optional[InputSchemaMessageTypeURLFieldSettings] = None
    """Settings for the url field."""


InputSchema: TypeAlias = Union[
    InputSchemaMessageTypeBooleanField,
    InputSchemaMessageTypeButtonField,
    InputSchemaMessageTypeImageField,
    InputSchemaMessageTypeJsonField,
    InputSchemaMessageTypeMarkdownField,
    InputSchemaMessageTypeMultiSelectField,
    InputSchemaMessageTypeSelectField,
    MessageTypeTextField,
    InputSchemaMessageTypeTextareaField,
    InputSchemaMessageTypeURLField,
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
