# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.message_type_url_field import MessageTypeURLField
from .shared.message_type_json_field import MessageTypeJsonField
from .shared.message_type_list_field import MessageTypeListField
from .shared.message_type_text_field import MessageTypeTextField
from .shared.message_type_color_field import MessageTypeColorField
from .shared.message_type_image_field import MessageTypeImageField
from .shared.message_type_button_field import MessageTypeButtonField
from .shared.message_type_number_field import MessageTypeNumberField
from .shared.message_type_select_field import MessageTypeSelectField
from .shared.message_type_boolean_field import MessageTypeBooleanField
from .shared.message_type_markdown_field import MessageTypeMarkdownField
from .shared.message_type_textarea_field import MessageTypeTextareaField
from .shared.message_type_multi_select_field import MessageTypeMultiSelectField

__all__ = ["MessageTypeVariant", "Field"]

Field: TypeAlias = Union[
    MessageTypeListField,
    MessageTypeSelectField,
    MessageTypeBooleanField,
    MessageTypeJsonField,
    MessageTypeNumberField,
    MessageTypeTextField,
    MessageTypeImageField,
    MessageTypeColorField,
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
