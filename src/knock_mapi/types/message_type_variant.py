# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .message_type_text_field import MessageTypeTextField

__all__ = [
    "MessageTypeVariant",
    "Field",
    "FieldMessageTypeBooleanField",
    "FieldMessageTypeBooleanFieldSettings",
    "FieldMessageTypeButtonField",
    "FieldMessageTypeButtonFieldSettings",
    "FieldMessageTypeImageField",
    "FieldMessageTypeImageFieldURL",
    "FieldMessageTypeImageFieldURLSettings",
    "FieldMessageTypeImageFieldSettings",
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


class FieldMessageTypeBooleanFieldSettings(BaseModel):
    default: Optional[bool] = None
    """The default value of the boolean field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeBooleanField(BaseModel):
    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["boolean"]
    """The type of the field."""

    settings: Optional[FieldMessageTypeBooleanFieldSettings] = None
    """Settings for the boolean field."""


class FieldMessageTypeButtonFieldSettings(BaseModel):
    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeButtonField(BaseModel):
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

    settings: Optional[FieldMessageTypeButtonFieldSettings] = None
    """Settings for the button field."""


class FieldMessageTypeImageFieldURLSettings(BaseModel):
    default: Optional[str] = None
    """The default value of the URL field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeImageFieldURL(BaseModel):
    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["url"]
    """The type of the field."""

    settings: Optional[FieldMessageTypeImageFieldURLSettings] = None
    """Settings for the url field."""


class FieldMessageTypeImageFieldSettings(BaseModel):
    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeImageField(BaseModel):
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

    url: FieldMessageTypeImageFieldURL
    """A URL field used in a message type."""

    settings: Optional[FieldMessageTypeImageFieldSettings] = None
    """Settings for the image field."""


class FieldMessageTypeMarkdownFieldSettings(BaseModel):
    default: Optional[str] = None
    """The default value of the markdown field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeMarkdownField(BaseModel):
    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["markdown"]
    """The type of the field."""

    settings: Optional[FieldMessageTypeMarkdownFieldSettings] = None
    """Settings for the markdown field."""


class FieldMessageTypeMultiSelectFieldSettingsOption(BaseModel):
    value: str
    """The value for the option."""

    label: Optional[str] = None
    """The display label for the option."""


class FieldMessageTypeMultiSelectFieldSettings(BaseModel):
    default: Optional[List[str]] = None
    """The default values for the multi-select field."""

    description: Optional[str] = None

    options: Optional[List[FieldMessageTypeMultiSelectFieldSettingsOption]] = None
    """The available options for the multi-select field."""

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeMultiSelectField(BaseModel):
    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    settings: FieldMessageTypeMultiSelectFieldSettings
    """Settings for the multi_select field."""

    type: Literal["multi_select"]
    """The type of the field."""


class FieldMessageTypeSelectFieldSettingsOption(BaseModel):
    value: str
    """The value for the option."""

    label: Optional[str] = None
    """The display label for the option."""


class FieldMessageTypeSelectFieldSettings(BaseModel):
    default: Optional[str] = None
    """The default value for the select field."""

    description: Optional[str] = None

    options: Optional[List[FieldMessageTypeSelectFieldSettingsOption]] = None
    """The available options for the select field."""

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeSelectField(BaseModel):
    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    settings: FieldMessageTypeSelectFieldSettings
    """Settings for the select field."""

    type: Literal["select"]
    """The type of the field."""


class FieldMessageTypeTextareaFieldSettings(BaseModel):
    default: Optional[str] = None
    """The default value of the textarea field."""

    description: Optional[str] = None

    max_length: Optional[int] = None

    min_length: Optional[int] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeTextareaField(BaseModel):
    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["textarea"]
    """The type of the field."""

    settings: Optional[FieldMessageTypeTextareaFieldSettings] = None
    """Settings for the textarea field."""


class FieldMessageTypeURLFieldSettings(BaseModel):
    default: Optional[str] = None
    """The default value of the URL field."""

    description: Optional[str] = None

    required: Optional[bool] = None
    """Whether the field is required."""


class FieldMessageTypeURLField(BaseModel):
    key: str
    """The unique key of the field."""

    label: Optional[str] = None
    """The label of the field."""

    type: Literal["url"]
    """The type of the field."""

    settings: Optional[FieldMessageTypeURLFieldSettings] = None
    """Settings for the url field."""


Field: TypeAlias = Union[
    FieldMessageTypeBooleanField,
    FieldMessageTypeButtonField,
    FieldMessageTypeImageField,
    FieldMessageTypeMarkdownField,
    FieldMessageTypeMultiSelectField,
    FieldMessageTypeSelectField,
    MessageTypeTextField,
    FieldMessageTypeTextareaField,
    FieldMessageTypeURLField,
]


class MessageTypeVariant(BaseModel):
    fields: List[Field]
    """The field types available for the variant."""

    key: str
    """The unique key string for the variant.

    Must be at minimum 3 characters and at maximum 255 characters in length. Must be
    in the format of ^[a-z0-9_-]+$.
    """

    name: str
    """A name for the variant. Must be at maximum 255 characters in length."""
